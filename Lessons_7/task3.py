# Task 3 - A simple calculator.
# Create a function called make_operation, which takes in a simple
# arithmetic operator as a first parameter (to keep things simple let it
# only be '+', '-' or '*') and an arbitrary number of arguments
# (only numbers) as the second parameter. Then return the sum or product
# of all the numbers in the arbitrary parameter. For example:
#
# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42

def make_operation(operator_str, num_1, num_2, *args):  # 3 required positional argument
    result = None
    arguments = [num_2, *args]

    if operator_str in ['+', '-', '*'] and isinstance(num_1, int):
        result = num_1
    else:
        print('Wrong type of arguments!!!')
        return None

    for number in arguments:
        if isinstance(number, int):
            if operator_str == '+':
                result += number
            elif operator_str == '-':
                result -= number
            elif operator_str == '*':
                result *= number
        else:
            print('Wrong type of arguments!!!')
            return None
    return result


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('-', 5, 'a', -10, -20))
print(make_operation('*', 7, 6))
