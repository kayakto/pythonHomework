import re
import doctest

def is_valid(color: str) -> bool:
    """
    Проверяет, корректен ли цвет по определенным критериям.
    :param color: Цвет для проверки.
    :return: True, если цвет корректный, иначе False.

    Тесты:
    >>> is_valid('#21f48D')
    True
    >>> is_valid('#888')
    True
    >>> is_valid('rgb(255, 255, 255)')
    True
    >>> is_valid('rgb(10%, 20%, 0%)')
    True
    >>> is_valid('hsl(200,100%,50%)')
    True
    >>> is_valid('hsl(0, 0%, 0%)')
    True
    >>> is_valid('#2345')
    False
    >>> is_valid('ffffff')
    False
    >>> is_valid('rgb(257, 50, 10)')
    False
    >>> is_valid('hsl(20, 10, 0.5)')
    False
    >>> is_valid('hsl(34%, 20%, 50%)')
    False
    """
    if bool(re.match(r'#', color)):
        pattern = re.compile(r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$')
        return bool(pattern.match(color))

    if bool(re.match(r'hsl', color)):
        pattern = re.compile(r'^hsl\((\d{1,3}|[1-9]\d{0,2}),\s*(100%|[1-9]?\d%|0%),\s*(100%|[1-9]?\d%|0%)\)$')
        return bool(pattern.match(color))

    if bool(re.match(r'rgb', color)):
        pattern = re.compile(r'^rgb\((\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), (\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), (\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?)\)$')
        return bool(pattern.match(color))
    
    return False


doctest.testmod()