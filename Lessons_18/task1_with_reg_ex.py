"""Task 1
Create a class method named 'validate', which should be called from the 
'__init__' method to validate parameter email, passed to the constructor.
The logic inside the 'validate' method could be to check if the passed email
parameter is a valid email string.
"""

import re


class User:
    """Create user object"""

    def __init__(self, login, name, email):
        self.login = login
        self.name = name
        self.email = User.validate(email) or "Wrong email format!"

    def talk(self):
        """Print user greeting"""
        print(
            f"Hello, I am {self.name}! My user login {self.login}.\n"
            f"You can send me email: {self.email}"
        )

    @classmethod
    def validate(cls, email):
        """Check if the passed email parameter is a valid email string"""
        if isinstance(email, str):
            email_regex_string = (
                r"([A-Za-z0-9]+[-._])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
            )
            match = re.fullmatch(email_regex_string, email)
            if match:
                return email
        return ''


user = User("Kotyhoroshko", "Ivan", "ivan.kotyhoroh@mail.com")
user.talk()

assert User.validate("abc-@mail.com") == ''
assert User.validate("abc..def@mail.com") == ''
assert User.validate(".abc@mail.com") == ''
assert User.validate("abc-@mail.com") == ''
assert User.validate("abc#def@mail.com") == ''
assert User.validate("abc.def@mail.7com") == ''

assert User.validate("abc.def@mail.com") == "abc.def@mail.com"
assert User.validate("abc-d@mail.com") == "abc-d@mail.com"
assert User.validate("abc@mail.com") == "abc@mail.com"
assert User.validate("abc_def@mail.com") == "abc_def@mail.com"
assert User.validate("abc.def44@4mail.com") == "abc.def44@4mail.com"

assert User.validate("abc.def@mail.c") == ''
assert User.validate("abc.def@mail#archive.com") == ''
assert User.validate("abc.def@mail") == ''
assert User.validate("abc.def@mail..com") == ''

assert User.validate("abc.def@mail.cc") == "abc.def@mail.cc"
assert User.validate("abc.def@mail-archive.com") == "abc.def@mail-archive.com"
assert User.validate("abc.def@mail.org") == "abc.def@mail.org"
assert User.validate("abc.def@mail.com") == "abc.def@mail.com"
