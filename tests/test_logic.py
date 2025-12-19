import pytest

def get_movie_rating_label(score):
    if score >= 8: return "Kiváló"
    elif score >= 5: return "Átlagos"
    else: return "Gyenge"

@pytest.mark.parametrize("score, expected", [
    (9, "Kiváló"),
    (6, "Átlagos"),
    (2, "Gyenge"),
    (8, "Kiváló"),
])
def test_movie_rating_logic(score, expected):
    assert get_movie_rating_label(score) == expected

def test_simple_structure():
    movie = {"title": "Tenet", "genre": "Sci-fi"}
    assert "title" in movie
    assert movie["genre"] == "Sci-fi"