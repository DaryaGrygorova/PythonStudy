# Math quiz (another version)

import random

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

if num_1 < num_2:
    num_1, num_2 = num_2, num_1

operators = '+-/*'
operator = random.choice(operators)


def expression(number_1, number_2, raw_operator):
    if raw_operator == '+':
        return number_1 + number_2
    elif raw_operator == '-':
        if number_1 < number_2:
            number_1, number_2 = number_2, number_1
        return number_1 - number_2
    elif raw_operator == '*':
        return number_1 * number_2
    elif raw_operator == '/':
        if number_1 < number_2:
            number_1, number_2 = number_2, number_1
        return round(number_1 / number_2, 1)         # round to one char after dot


right_result = expression(num_1, num_2, operator)

# # Another way to get expression (with lambda-function )

# operators_map = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: round(a / b)
# }

# right_result = operators_map[operator](num_1, num_2)

user_answer = input(
    'Please enter the result of expression (use one char after point):\n'
    f'{num_1} {operator} {num_2}\n'
    ).replace(',', '.')     # check a case of using a comma instead of a dot


# # Compare results as a string

# # 1
# check a case of using a comma (or a dot) zero for integer number
raw_right_result = str(right_result)
if (
    user_answer == raw_right_result
    or user_answer == raw_right_result + '.0'
    or user_answer + '.0' == raw_right_result
   ):
    print('Congrats!')
else:
    print(f'Wrong answer! Right result: {raw_right_result}')


# # 2
# # check a case of using a comma (or a dot) zero for integer number
# raw_user_answer = user_answer + '.0' if user_answer.isdigit() and operator == '/' else user_answer
#
# if str(right_result) == raw_user_answer:
#     print('Congrats!')
# else:
#     print(f'Wrong answer! Right result: {str(right_result)}')
#

# # Compare results as an integer/float
# answer = None
# try:
#     answer = float(user_answer)
#     if answer == right_result:
#         print('Congrats!')
#     else:
#         print(f'Wrong answer! Right result: {str(right_result)}')
# except ValueError:
#     print('Wrong format! Try again!')
