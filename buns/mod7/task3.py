import time

def validate_args(funk):
    def wrapped_funk(*args, **kwargs):
        count = len(args)
        if count < 1:
            return "Not enough arguments"
        elif count > 1:
            return "Too many arguments"
        argument = args[0]
        if not(isinstance(argument, int)):
            return "Wrong types"
        if argument < 0:
            return "Negative argument"
        return funk(*args, **kwargs)
    return wrapped_funk

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

class Timer:
    def __init__(self, func):
        self.func = func
        self.start_time = None
        self.end_time = None

    def __call__(self, *args, **kwargs):
        if self.start_time is None:
            self.start_time = time.time()
            result = self.func(*args, **kwargs)
            self.end_time = time.time()
            print(f"Функция {self.func.__name__} выполнилась за {self.end_time - self.start_time} секунд")
            self.start_time = None
            self.end_time = None
        else:
            result = self.func(*args, **kwargs)
        return result

@Timer
@memoize
@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
