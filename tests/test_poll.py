import pytest
from app.models.poll import Poll
from datetime import datetime

@pytest.fixture
def new_poll():
    return Poll(question="Czy lubisz testy?", created_at=datetime(2023, 1, 1, 12, 0, 0))

def test_poll_creation(new_poll):
    assert new_poll.question == "Czy lubisz testy?"
    assert isinstance(new_poll.created_at, datetime)
    assert isinstance(new_poll, Poll) 