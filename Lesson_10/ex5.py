"""
Чи є рік високосним на планеті, якщо ми знаємо період обертання планети
"""


def is_leap_year(d, y):
    """
    Чи є рік високосним на планеті, якщо ми знаємо період обертання планети
    """
    # return y * d == int(y * d)
    # return y * d % 1 == 0
    return (y * d).is_integer()


print(is_leap_year(365.25, 2018))
print(is_leap_year(365.25, 2020))
print(is_leap_year(124.5, 102))
print(is_leap_year(124.125, 102))
