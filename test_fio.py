from initials import fio
import pytest

@pytest.mark.parametrize(
    ('initials', 'expected'),
    [
        (['Иванов', 'Иван', 'Иванович'], 'ИИИ'),
        (['Жан', 'Клот', 'Вандамович'], 'ЖКВ'),
    ]
)
def test_initial(initials, expected):
    assert fio(initials) == expected, 'Error'
