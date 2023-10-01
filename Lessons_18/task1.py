"""Task 1
Create a class method named 'validate', which should be called from the 
'__init__' method to validate parameter email, passed to the constructor.
The logic inside the 'validate' method could be to check if the passed email
parameter is a valid email string.
"""


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

    @staticmethod
    def email_to_part(email):
        """Return tuple that includes prefix, and two part of domain from email address"""
        if email.count("@"):
            sep_index = email.index("@")
            prefix = email[0:sep_index]
            domain = email[sep_index + 1:]
            if domain.count("."):
                point_index = domain.index(".")
                domain_name = domain[:point_index]
                top_level_domain = domain[point_index + 1:]
                if (
                    len(prefix) > 2
                    and len(domain_name) > 0
                    and len(top_level_domain) >= 2
                ):
                    return prefix, domain_name, top_level_domain
        return None, None, None

    @staticmethod
    def check_email_part(part, symbols_list, with_num=True):
        """Check if the passed email part is a valid string. Return True or False"""
        def valid_char(char):
            if with_num:
                return char.isalpha() or char.isdigit()
            return char.isalpha()

        if valid_char(part[0]) and valid_char(part[-1]):
            for index in range(1, len(part) - 1):
                if (
                    valid_char(part[index])
                    or part[index] in symbols_list
                    and valid_char(part[index - 1])
                ):
                    continue
                break
            else:
                return True
        return False

    @classmethod
    def validate(cls, email):
        """Check if the passed email parameter is a valid email string"""
        if isinstance(email, str):
            prefix, domain_name, top_level_domain = cls.email_to_part(email)
            if prefix and domain_name and top_level_domain:
                if (
                    cls.check_email_part(prefix, [".", "-", "_"])
                    and cls.check_email_part(domain_name, ["-"])
                    and cls.check_email_part(top_level_domain, [], with_num=False)
                ):
                    return email
        return ''


user = User("Kotyhoroshko", "Ivan", "ivan.kotyhoroh@mail.com")
user.talk()

assert User.validate("abc-@mail.com") == ''
assert User.validate("abc..def@mail.com") == ''
assert User.validate(".abc@mail.com") == ''
assert User.validate("abc#def@mail.com") == ''
assert User.validate("abc.def@mail.7com") == ''

assert User.validate("abc.def@mail.com") == "abc.def@mail.com"
assert User.validate("abc-d@mail.com") == "abc-d@mail.com"
assert User.validate("abc@mail.com") == "abc@mail.com"
assert User.validate("abc_def@mail.com") == "abc_def@mail.com"
assert User.validate("abc.def44@4mail.com") == "abc.def44@4mail.com"
#
assert User.validate("abc.def@mail.c") == ''
assert User.validate("abc.def@mail#archive.com") == ''
assert User.validate("abc.def@mail") == ''
assert User.validate("abc.def@mail..com") == ''

assert User.validate("abc.def@mail.cc") == "abc.def@mail.cc"
assert User.validate("abc.def@mail-archive.com") == "abc.def@mail-archive.com"
assert User.validate("abc.def@mail.org") == "abc.def@mail.org"
assert User.validate("abc.def@mail.com") == "abc.def@mail.com"
