import pytest
from app import create_app, db
from app.models.poll import Poll
from app.models.answer_option import AnswerOption
from app.models.category import Category

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # przykładowe dane testowe
            cat = Category(name="Testowa kategoria")
            db.session.add(cat)
            db.session.commit()

            poll = Poll(question="Czy lubisz testy?", category_id=cat.id)
            db.session.add(poll)
            db.session.commit()

            option = AnswerOption(text="Tak", poll_id=poll.id)
            db.session.add(option)
            db.session.commit()

        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_list_polls(client):
    response = client.get('/polls')
    assert response.status_code == 200
    assert b"Czy lubisz testy?" in response.data

def test_list_options_valid_poll(client):
    response = client.get('/polls/1/options')
    assert response.status_code == 200
    assert b"Tak" in response.data

def test_list_options_invalid_poll(client):
    response = client.get('/polls/999/options')
    assert response.status_code == 404

def test_list_categories(client):
    response = client.get('/categories')
    assert response.status_code == 200
    assert b"Testowa kategoria" in response.data