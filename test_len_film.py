from len_film import longest_film
import pytest

@pytest.mark.parametrize(
    ('film1', 'film2', 'film3', 'expected'),
    [
        ('Война миров', 'Рио', 'Сияние', 'Война миров'),
        ('Гарри потер', 'Восток', 'Казань', 'Гарри потер')
    ]
)
def test_len_films(film1, film2, film3, expected):
    assert longest_film(film1, film2, film3) == expected, 'Error'