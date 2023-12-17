"""
Task 2
Write a function that takes in two numbers from the user via input(),
call the numbers a and b, and then returns the value of squared
a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers,
and if value b was zero (cannot divide by zero).
"""


def user_numbers():
    """Function that takes in two numbers from the user via input(),
    call the numbers a and b, and then returns the value of squared
    a divided by b"""
    try:
        a = int(input(r"Please, enter the number: "))
        b = int(input(r"Please, enter another number: "))
    except ValueError:
        print("ERROR: Wrong format of argument(s)\n")
    else:
        try:
            return round(a**2 / b, 2)
        except ZeroDivisionError:
            print("ERROR: Cannot divide by zero\n")
    return None


while True:
    result = user_numbers()
    if result:
        print(f"a**2/b = {result} \n")
