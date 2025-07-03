from app.models.poll import Poll
from app.models.answer_option import AnswerOption

def test_poll_vote_result_flow(client, app):
    # 1. Utwórz nową ankietę przez POST
    response = client.post('/polls/create', data={
        'question': 'Czy lubisz testy?',
        'options[]': ['Tak', 'Nie']
    }, follow_redirects=True)

    assert response.status_code == 200
    assert 'Czy lubisz testy?' in response.get_data(as_text=True)

    # 2. Pobierz ostatnią ankietę z bazy
    with app.app_context():
        poll = Poll.query.order_by(Poll.id.desc()).first()
        assert poll is not None
        assert poll.question == 'Czy lubisz testy?'

        # Upewnij się, że są dwie opcje odpowiedzi
        assert len(poll.answer_options) == 2
        option = poll.answer_options[0]

    # 3. Oddaj głos na jedną z opcji
    vote_response = client.post( f'/polls/{poll.id}/vote', data={'answer': option.id}, follow_redirects=True )
    assert vote_response.status_code == 200
    # assert 'Dziękujemy za oddanie głosu' in vote_response.get_data(as_text=True)

    # 4. Sprawdź wyniki ankiety
    result_response = client.get(f'/polls/{poll.id}/results')
    assert result_response.status_code == 200
    assert option.text in result_response.get_data(as_text=True)
    assert "1 głos" in result_response.get_data(as_text=True)
