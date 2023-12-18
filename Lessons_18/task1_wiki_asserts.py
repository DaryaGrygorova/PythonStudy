"""Task 1
Create a class method named 'validate', which should be called from the 
'__init__' method to validate parameter email, passed to the constructor.
The logic inside the 'validate' method could be to check if the passed email
parameter is a valid email string.
Email validations: https://en.wikipedia.org/wiki/Email_address
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
        split_char = None
        if email[0] == '"' and email.count('"@') == 1:
            split_char = '"@'

        elif email.count("@") == 1:
            split_char = "@"

        if split_char:
            prefix, domain = email.split(split_char)
            if domain.count("."):
                domain_names = domain.split(".")
                top_level_domain = domain_names.pop()
                if (
                    64 > len(prefix) >= 1
                    and len(domain_names) > 0
                    and len(top_level_domain) >= 2
                ):
                    return prefix, domain_names, top_level_domain

        return None, None, None

    @staticmethod
    def check_email_part(part, part_name="top_level_domain", with_num=True):
        """Check if the passed email part is a valid string. Return True or False"""
        symbols_list = {
            "prefix": [
                ".",
                "!",
                "#",
                "$",
                "%",
                "&",
                "'",
                "*",
                "+",
                "-",
                "/",
                "=",
                "?",
                "^",
                "_",
                "`",
                "{",
                "|",
                "}",
                "~",
            ],
            "domain": ["-"],
            "top_level_domain": [],
        }

        def valid_char(char):
            if with_num:
                return char.isalpha() or char.isdigit()
            return char.isalpha()

        if part_name == "prefix" and part[0] == '"':
            for index in range(1, len(part) - 1):
                if valid_char(part[index]) or part[index] in symbols_list[part_name] + [
                    " ",
                    r'"',
                    "(",
                    ")",
                    ",",
                    ":",
                    ";",
                    "<",
                    ">",
                    "@",
                    "[",
                    "\\",
                    "]",
                ]:
                    continue
                break
            else:
                return True

        elif (
            part
            and valid_char(part[0])
            and (valid_char(part[-1]) or part[-1] in symbols_list[part_name])
        ):
            for index in range(1, len(part) - 1):
                if (
                    valid_char(part[index])
                    or part[index] in symbols_list[part_name]
                    and (valid_char(part[index - 1]))
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
            prefix, domain_names, top_level_domain = cls.email_to_part(email)
            if prefix and domain_names and top_level_domain:
                if (
                    cls.check_email_part(prefix, "prefix")
                    and all(
                        cls.check_email_part(name, "domain") for name in domain_names
                    )
                    and cls.check_email_part(
                        top_level_domain, "top_level_domain", with_num=False
                    )
                ):
                    return email
        return ""


# Invalid email
assert User.validate("abc.example.com") == ""
assert User.validate("a@b@c@example.com") == ""
assert User.validate(r'a"b(c)d,e:f;g<h>i[j\k]l@example.com') == ""
assert User.validate('just"not"right@example.com') == ""
assert User.validate('this is"not\allowed@example.com') == ""
assert User.validate(r'this\ still"not\\allowed@example.com') == ""
assert (
    User.validate(
        "1234567890123456789012345678901234567890123456789012345678901234+x@example.com"
    )
    == ""
)
assert User.validate("i.like.underscores@but_they_are_not_allowed_in_this_part") == ""
assert User.validate("abc..e@example.com") == ""

# Valid email
assert User.validate("simple@example.com") == "simple@example.com"
assert User.validate("very.common@example.com") == "very.common@example.com"
assert User.validate("x@example.com") == "x@example.com"
assert (
    User.validate("ong.email-address-with-hyphens@and.subdomains.example.com")
    == "ong.email-address-with-hyphens@and.subdomains.example.com"
)
assert (
    User.validate("user.name+tag+sorting@example.com")
    == "user.name+tag+sorting@example.com"
)
assert User.validate("name/surname@example.com") == "name/surname@example.com"
assert User.validate('" "@example.org') == '" "@example.org'
assert User.validate('"john..doe"@example.org') == '"john..doe"@example.org'
assert User.validate("mailhost!username@example.org") == "mailhost!username@example.org"
assert (
    User.validate(
        r'"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com'
    )
    == r'"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com'
)
assert User.validate("user%example.com@example.org") == "user%example.com@example.org"
assert User.validate("user-@example.org") == "user-@example.org"

# Not implemented cases for next valid emails:
# IP addresses are allowed instead of domains when in square brackets, but strongly discouraged
# assert User.validate("postmaster@[123.123.123.123]") == "postmaster@[123.123.123.123]"

# IPv6 uses a different syntax
# assert
#   User.validate(
#       "postmaster@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]"
#   )
#   == "postmaster@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]"

# local domain name with no TLD, although ICANN highly discourages dotless email addresses
# assert User.validate("admin@example") == "admin@example"

# emoji are only allowed with SMTPUTF8
# assert User.validate('I❤️CHOCOLATE🍫@example.com') == 'I❤️CHOCOLATE🍫@example.com'
