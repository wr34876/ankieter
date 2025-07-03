import pytest
from app.models.poll import Poll
from app.models.answer_option import AnswerOption
from app import db

#test opinii użytkownika (feedback)
def test_feedback_form_get(client):
    response = client.get('/feedback')
    assert response.status_code == 200
    assert b'Formularz opinii' in response.data


def test_feedback_form_post(client, app):
    response = client.post('/feedback', data={'message': 'Świetna aplikacja!'}, follow_redirects=True)
    assert response.status_code == 200
    assert 'Dziękujemy za opinię' in response.get_data( as_text=True )

    with app.app_context():
        from app.models.user_feedback import UserFeedback
        feedback = UserFeedback.query.filter_by(message='Świetna aplikacja!').first()
        assert feedback is not None


def test_feedback_form_post_empty_message(client):
    response = client.post('/feedback', data={'message': ''})
    assert response.status_code == 400
    assert 'Wiadomość nie może być pusta' in response.get_data(as_text=True)