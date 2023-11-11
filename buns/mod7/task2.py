def memoize(func):
    '''Декоратор, который принимает функцию в качестве аргумента и возвращает функцию-оболочку'''

    dict_cashe = {}

    def wrapped_funk(*args, **kwargs):
        tuple = (args, frozenset(kwargs.items()))
        if tuple in dict_cashe:
            return dict_cashe[tuple]
        result = func(*args, **kwargs)
        dict_cashe[tuple] = result
        return result
    wrapped_funk.__name__ = func.__name__
    wrapped_funk.__doc__ = func.__doc__
    return wrapped_funk

@memoize
def fibonacci(n):
    '''Рекурсивная функция фибоначчи'''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

