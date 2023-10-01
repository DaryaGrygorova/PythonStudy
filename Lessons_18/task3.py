"""Task 3
Write a class TypeDecorators which has several methods for converting
results of functions to a specified type (if it's possible):
methods:
to_int
to_str
to_bool
to_float

Don't forget to use @wraps
"""

from functools import wraps


class TypeDecorators:
    """Convert result of function to a specified type"""

    @staticmethod
    def to_int(func):
        """Convert value to integer type"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return int(res)

        return wrapper

    @staticmethod
    def to_str(func):
        """Convert value to string type"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return str(res)

        return wrapper

    @staticmethod
    def to_bool(func):
        """Convert value to bool type"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return bool(res)

        return wrapper

    @staticmethod
    def to_float(func):
        """Convert value to float type"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return float(res)

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    """Return own argument"""
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    """Return own argument"""
    return string


@TypeDecorators.to_str
def do_another_nothing(number: int):
    """Return own argument"""
    return number


@TypeDecorators.to_float
def do_another_something(string: str):
    """Return own argument"""
    return string


assert do_nothing("25") == 25
assert do_something("True") is True
assert do_another_nothing(85) == "85"
assert do_another_something("78.33") == 78.33
