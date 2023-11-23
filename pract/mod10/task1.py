import re
import doctest

def check_password(password: str) -> bool:
    """
    Проверяет, корректен ли пароль по определенным критериям.
    :param password: Пароль для проверки.
    :return: True, если пароль корректный, иначе False.

    Тесты:
    >>> check_password("rtG3FG!Tr^e")
    True
    >>> check_password("aA1!*!1Aa")
    True
    >>> check_password("oF^a1D@y5e6")
    True
    >>> check_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> check_password("пароль")
    False
    >>> check_password("password")
    False
    >>> check_password("qwerty")
    False
    >>> check_password("lOngPa$$$W0Rd")
    False
    >>> check_password("Земля плоская")
    False
    >>> check_password("123456")
    False
    """
    if not re.match(r'^[a-zA-Z0-9^$%@#&*!?]+$', password):
        return False

    if len(password) < 6:
        return False

    if len(re.findall(r'[A-Z]', password)) < 2:
        return False

    if not re.search(r'\d', password):
        return False

    if len(set(re.findall(r'[^a-zA-Z0-9]', password))) < 2:
        return False

    if re.search(r'(.)\1\1', password):
        return False
    return True

doctest.testmod()