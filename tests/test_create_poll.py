import pytest
from app.models.poll import Poll
from app.models.answer_option import AnswerOption
from app import db

def test_create_poll_get(client):
    response = client.get('/polls/create')
    assert response.status_code == 200
    assert "Utwórz nową ankietę" in response.data.decode('utf-8')  # dopasuj tekst do swojej strony

def test_create_poll_post_valid(client, app):
    data = {
        'question': 'Czy lubisz testować?',
        'options[]': ['Tak', 'Nie', 'Może']
    }
    response = client.post('/polls/create', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert "Ankieter" in response.data.decode('utf-8')  # np. tytuł strony głównej lub inny znak sukcesu

    with app.app_context():
        poll = Poll.query.filter_by(question='Czy lubisz testować?').first()
        assert poll is not None
        options = AnswerOption.query.filter_by(poll_id=poll.id).all()
        assert len(options) == 3
        texts = [opt.text for opt in options]
        assert 'Tak' in texts
        assert 'Nie' in texts
        assert 'Może' in texts

@pytest.mark.parametrize("post_data, error_msg", [
    ({'question': '', 'options[]': ['Tak', 'Nie']}, "Wypełnij pytanie i dodaj minimum 2 opcje odpowiedzi"),
    ({'question': 'Testowe pytanie', 'options[]': ['']}, "Wypełnij pytanie i dodaj minimum 2 opcje odpowiedzi"),
    ({'question': 'Testowe pytanie', 'options[]': ['Tak']}, "Wypełnij pytanie i dodaj minimum 2 opcje odpowiedzi"),
])
def test_create_poll_post_invalid(client, post_data, error_msg):
    response = client.post('/polls/create', data=post_data)
    if error_msg:
        assert response.status_code == 400
        assert error_msg in response.data.decode('utf-8')
    else:
        # Jeśli brak komunikatu błędu – powinno przejść
        assert response.status_code in (200, 302)
