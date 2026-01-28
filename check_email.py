def check_email(email: str) -> bool:
    # Напишите ваш код здесь
    if '@' in email:
        if '.' in email:
            if ' ' in email:
                return False
            else:
                return True
        else:
            return False
    return False


if __name__ == '__main__':
    assert check_email('Helloworld@.ru') is True
    assert check_email('мояпочта@нетология.ру') is True
    assert check_email('python@email@net') is False
    assert check_email(' em@il.ru') is False
    print("\nОтличная работа, отправляйте на проверку!")