from check_email import check_email
import pytest

@pytest.mark.parametrize(
    ('email','expected'),
    [
        ('почта@mail. ru', False),
        ('почта@mail.ru', True),
    ]
)
def test_check_emails(email, expected):
    assert check_email(email) == expected, 'Error'