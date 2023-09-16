"""
Task 2
Write a Python program to access a function inside a function
(Tips: use function, which returns another function)
"""


def outer_func(user_name):
    """Returns greeting function for the user named 'user_name'"""

    def greeting_func(repeat=1):
        print(f"Hello, {user_name}!\n" * repeat)

    return greeting_func


greeting_user = outer_func("Bob")
greeting_user(repeat=3)
