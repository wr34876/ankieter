import pytest
from app.models.answer_option import AnswerOption

@pytest.fixture
def new_answer_option():
    return AnswerOption(text="Tak", poll_id=1, votes=5)

def test_answer_option_creation(new_answer_option):
    assert new_answer_option.text == "Tak"
    assert new_answer_option.poll_id == 1
    assert new_answer_option.votes == 5
    assert isinstance(new_answer_option, AnswerOption) 