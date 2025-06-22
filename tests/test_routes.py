import pytest
from app import create_app, db
from app.models.poll import Poll
from app.models.answer_option import AnswerOption
from app.models.category import Category

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.create_all()
        # Dodaj testowe dane
        cat = Category(name="Testowa kategoria")
        db.session.add(cat)
        poll = Poll(question="Testowe pytanie?", category=cat)
        db.session.add(poll)
        option1 = AnswerOption(text="Opcja 1", poll=poll, votes=3)
        option2 = AnswerOption(text="Opcja 2", poll=poll, votes=5)
        db.session.add_all([option1, option2])
        db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Witamy w aplikacji Ankieter" in response.data

def test_list_polls(client):
    response = client.get('/polls')
    assert response.status_code == 200
    assert b"Testowe pytanie?" in response.data

def test_list_options(client):
    # Zakładamy, że Poll o id=1 istnieje (z fixture)
    response = client.get('/polls/1/options')
    assert response.status_code == 200
    assert b"Opcja 1" in response.data
    assert b"Opcja 2" in response.data

def test_list_categories(client):
    response = client.get('/categories')
    assert response.status_code == 200
    assert b"Testowa kategoria" in response.data

def test_list_options_not_found(client):
    response = client.get('/polls/999/options')  # zakładamy, że 999 nie istnieje
    assert response.status_code == 404


'''
#test dla nieistniejącego poll_id w /polls/<int:poll_id>/options

def test_vote_option(client, app):
    # Przykład oddania głosu na opcję o id=1
    with app.app_context():
        option = AnswerOption.query.first()
        initial_votes = option.votes

    response = client.post(f'/polls/{option.poll_id}/vote', data={'option_id': option.id})
    assert response.status_code == 302  # zakładamy przekierowanie po głosowaniu

    with app.app_context():
        updated_option = AnswerOption.query.get(option.id)
        assert updated_option.votes == initial_votes + 1


#testy formularza głosowania, jeśli jest endpoint do przyjmowania głosu
#zakładając, że istnieje endpoint /polls/<int:poll_id>/vote (POST)

def test_vote_option(client, app):
    # Przykład oddania głosu na opcję o id=1
    with app.app_context():
        option = AnswerOption.query.first()
        initial_votes = option.votes

    response = client.post(f'/polls/{option.poll_id}/vote', data={'option_id': option.id})
    assert response.status_code == 302  # zakładamy przekierowanie po głosowaniu

    with app.app_context():
        updated_option = AnswerOption.query.get(option.id)
        assert updated_option.votes == initial_votes + 1

#test opinii użytkownika (feedback)
#jeśli istnieje endpoint np. /feedback (POST i GET)

def test_feedback_form_get(client):
    response = client.get('/feedback')
    assert response.status_code == 200
    assert b'Formularz opinii' in response.data  # zakładamy taki tekst w szablonie

def test_feedback_form_post(client, app):
    response = client.post('/feedback', data={'message': 'Super aplikacja!'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Dziękujemy za opinię' in response.data

    with app.app_context():
        from app.models.user_feedback import UserFeedback
        feedback = UserFeedback.query.filter_by(message='Super aplikacja!').first()
        assert feedback is not None


'''