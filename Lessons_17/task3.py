"""Task 3 - Fraction
Створіть клас Fraction, який буде представляти всю базову
арифметичну логіку для дробів (+, -, /, *) з належною перевіркою
й обробкою помилок. Потрібно додати магічні методи для математичних
операцій та операції порівняння між об'єктами класу Fraction
"""
import math


class Fraction:
    """Create object that includes arithmetic methods for fractions (+, -, /, *)"""

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError(
                "Type of numerator, denominator of fraction must be integer!"
            )
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def reduction(numerator, denominator):
        """Return numerator, denominator after fractional reduction"""
        gcd = math.gcd(numerator, denominator)
        return int(numerator / gcd), int(denominator / gcd)

    def __add__(self, summand):
        if not isinstance(summand, Fraction) and not isinstance(summand, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(summand, int):
            summand = Fraction(summand, 1)

        denominator = math.lcm(self.denominator, summand.denominator)
        numerator = int(
            (self.numerator * denominator / self.denominator)
            + (summand.numerator * denominator / summand.denominator)
        )
        numerator, denominator = Fraction.reduction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __sub__(self, subtracted):
        if not isinstance(subtracted, Fraction) and not isinstance(subtracted, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(subtracted, int):
            subtracted = Fraction(subtracted, 1)

        denominator = math.lcm(self.denominator, subtracted.denominator)
        numerator = int(
            (self.numerator * denominator / self.denominator)
            - (subtracted.numerator * denominator / subtracted.denominator)
        )

        numerator, denominator = Fraction.reduction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, Fraction) and not isinstance(multiplier, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(multiplier, int):
            multiplier = Fraction(multiplier, 1)

        numerator = self.numerator * multiplier.numerator
        denominator = self.denominator * multiplier.denominator

        numerator, denominator = Fraction.reduction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __truediv__(self, divisor):
        if not isinstance(divisor, Fraction) and not isinstance(divisor, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(divisor, int):
            divisor = Fraction(divisor, 1)

        numerator = self.numerator * divisor.denominator
        denominator = self.denominator * divisor.numerator

        numerator, denominator = Fraction.reduction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        if not isinstance(other, Fraction) and not isinstance(other, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator_1, denominator_1 = Fraction.reduction(
            self.numerator, self.denominator
        )
        numerator_2, denominator_2 = Fraction.reduction(
            other.numerator, other.denominator
        )
        return numerator_1 == numerator_2 and denominator_1 == denominator_2

    def is_bigger(self, other):
        """Return True if self fraction bigger then other"""
        denominator = math.lcm(self.denominator, other.denominator)
        numerator_1 = self.numerator * denominator / self.denominator
        numerator_2 = other.numerator * denominator / other.denominator
        return numerator_1 > numerator_2

    def __str__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print("1/2 + 1/4 =", x + y)  # 1/2 + 1/4 == Fraction(3, 4)
    print("1/2 + 3 = ", x + 3)  # 1/2 + 3 == Fraction(7, 2)

    print("1/2 - 1/4 =", x - y)  # 1/2 - 1/4 == Fraction(1, 4)
    print("1/2 - 2 =", x - 2)  # 1/2 - 2 == Fraction(-3, 2)

    print("1/2 * 1/4 =", x * y)  # 1/2 * 1/4 == Fraction(1, 8)
    print("1/2 * 2 =", x * 3)  # 1/2 * 2 == Fraction(3, 2)

    print("1/4 / 1/2 =", y / x)  # 1/4 / 1/2 == Fraction(1, 2)
    print("1/2 / 3 =", x / 3)  # = Fraction(1, 6)

    print("Is 2/4 equal 1/2?: ", Fraction(2, 4) == Fraction(1, 2))  # True
    print("Is 4/2 equal 2?: ", Fraction(4, 2) == 2)  # True
    print("Is 2 equal 4/2?: ", 2 == Fraction(4, 2))  # True
    print("Is 3/2 equal 1/2?: ", Fraction(3, 2) == Fraction(1, 2))  # True

    print("Is 1/2 bigger then 1/4?: ", x.is_bigger(y))  # True
    print("Is 1/4 bigger then 1/2?: ", y.is_bigger(x))  # False
