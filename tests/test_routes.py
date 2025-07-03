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
    assert b"Ankieter" in response.data

'''
# Chwilowo wyłączamy
def test_list_polls(client):
    response = client.get('/polls')
    assert response.status_code == 200
    assert b"Testowe pytanie?" in response.data
'''

'''
# Chwilowo wyłączamy
def test_list_options(client):
    # Zakładamy, że Poll o id=1 istnieje (z fixture)
    response = client.get('/polls/1/options')
    assert response.status_code == 200
    assert b"Opcja 1" in response.data
    assert b"Opcja 2" in response.data
'''

def test_list_categories(client):
    response = client.get('/categories')
    assert response.status_code == 200
    assert b"Testowa kategoria" in response.data

def test_list_options_not_found(client):
    response = client.get('/polls/999/options')  # zakładamy, że 999 nie istnieje
    assert response.status_code == 404

def test_vote_option(client, app):
    with app.app_context():
        option = AnswerOption.query.first()
        initial_votes = option.votes

    response = client.post(f'/polls/{option.poll_id}/vote', data={'answer': option.id})
    assert response.status_code == 302  # zakładamy przekierowanie po głosowaniu

    with app.app_context():
        updated_option = AnswerOption.query.get(option.id)
        assert updated_option.votes == initial_votes + 1




def test_vote_valid_option(client, app):
    with app.app_context():
        from app.models.answer_option import AnswerOption
        option = AnswerOption.query.first()
        initial_votes = option.votes

    response = client.post(f'/polls/{option.poll_id}/vote', data={'answer': option.id}, follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        from app.models.answer_option import AnswerOption
        updated_option = AnswerOption.query.get(option.id)
        assert updated_option.votes == initial_votes + 1


def test_vote_missing_option(client):
    response = client.post('/polls/1/vote', data={}, follow_redirects=True)
    assert response.status_code == 400
    assert b'Nie wybrano odpowiedzi' in response.data


def test_vote_invalid_option(client):
    # Zakładamy, że poll_id=1 istnieje, ale option_id=999 nie
    response = client.post('/polls/1/vote', data={'answer': 999})
    assert response.status_code == 404

def test_delete_poll(client, app):
    with app.app_context():
        from app.models.poll import Poll
        poll = Poll.query.first()
        poll_id = poll.id

    response = client.post(f'/polls/{poll_id}/delete', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        from app.models.poll import Poll
        deleted_poll = Poll.query.get(poll_id)
        assert deleted_poll is None

