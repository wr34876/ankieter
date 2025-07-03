import pytest
from app.models.category import Category

@pytest.fixture
def new_category():
    return Category(name="Testowa kategoria")

def test_category_creation(new_category):
    assert new_category.name == "Testowa kategoria"
    assert isinstance(new_category, Category) 