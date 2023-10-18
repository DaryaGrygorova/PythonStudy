"""
Task 3
Write a decorator "arg_rules" that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False
and print the reason it failed; otherwise, return the result.
"""


def arg_rules(type_: type, max_length: int, contains: list):
    """Validates arguments passed to the function"""

    def wrapper(func):
        def check_agr(argument):
            if not isinstance(argument, type_):
                print(
                    f'Type of argument "{argument}" is not valid! It must be "{type_}"'
                )
                return False
            if len(argument) > max_length:
                print(
                    f'Argument "{argument}" is not valid!',
                    f'It must consist of no more than "{max_length}" characters',
                )
                return False
            for symbols in contains:
                if symbols not in argument:
                    print(
                        f'Argument "{argument}" is not valid! It must contain "{symbols}"'
                    )
                    return False
            res = func(argument)
            return res

        return check_agr

    return wrapper


@arg_rules(type_=str, max_length=15, contains=["05", "@"])
def create_slogan(name: str) -> str:
    """Create slogan for user with name 'name'"""
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("johndoe05@gmail.com") is False
assert create_slogan("S@SH05") == "S@SH05 drinks pepsi in his brand new BMW!"
