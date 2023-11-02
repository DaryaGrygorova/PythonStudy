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
    def to_type_factory(target_type):
        """Creates a functions that convert value to target type"""

        def to_type(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return target_type(func(*args, **kwargs))
                except ValueError:
                    return func(*args, **kwargs)

            return wrapper

        return to_type

    to_int = to_type_factory(int)
    to_str = to_type_factory(str)
    to_bool = to_type_factory(bool)
    to_float = to_type_factory(float)


@TypeDecorators.to_int
def do_nothing(string: str):
    """Return own argument"""
    return string


# Another way to use TypeDecorators.to_type_factory(type)
@TypeDecorators.to_type_factory(int)
def do_nothing2(string: str):
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
