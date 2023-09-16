"""
Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
"""


def logger(func):
    """Prints a function with arguments passed to it"""

    def wrapper(*args):
        print(
            f"Function '{func.__name__}' was called with argument(s): {''.join(str(args)[1:-1])}"
        )
        return func(*args)

    return wrapper


@logger
def add(x, y):
    """Return sum of arguments"""
    return x + y


@logger
def square_all(*args):
    """Returns list of the squares of the arguments"""
    return [arg**2 for arg in args]


add(4, 5)
square_all(2, 6, 7, 1, 3)
