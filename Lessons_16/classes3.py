"""Decorator @property"""


class Employee:
    """Create object employee"""

    def __init__(self, first, second):  # initialization
        self.first = first
        self.second = second
        # self.email = f'{self.first[0].lower()}{self.second.lower()}@email.com'

    @property
    # вбудований декоратор що при кожному виклику self.email перераховує
    # та повертає актуальне значення
    # ВАЖЛИВО!!! синтаксис звернення як для атрибуту (без дужок)
    def email(self):
        """Return email"""
        return f"{self.first[0].lower()}{self.second.lower()}@email.com"

    def full_name(self):
        """Return full name of employee"""
        return f"{self.first} {self.second}"


employee_1 = Employee("Jenny", "Smith")  # instantiation
print(employee_1.email)
print(employee_1.full_name())
print("____________")

employee_1.second = "Ford"
print(employee_1.email)
print(employee_1.full_name())
print("____________")
