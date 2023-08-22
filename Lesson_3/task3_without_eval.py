# Task 3 - The math quiz program.
# Write a program that asks the answer for a 
# mathematical expression, checks whether the user is right or wrong,
# and then responds with a message accordingly.

import random

print("Welcome to math quiz!!! For exit enter " r"'\x')")

COUNT_TOURS = 5
count_questions = 0
count_right_answers = 0

def create_expression():
    a = random.randrange(1, 11)
    b = random.randrange(1, 11)
    operator = random.choice(['*','//', '+', '-'])

    math_expression = f'{a} {operator} {b}'
    expression_result = ''

    match operator:
        case '*': 
            expression_result = str(a * b)
        case '//': 
            expression_result = str(a // b)
        case '+': 
            expression_result = str(a + b)
        case '-': 
            expression_result = str(a - b)

    return (math_expression, expression_result)


while count_questions < COUNT_TOURS:

    expression, right_answer = create_expression()

    answer = input(
        'Please enter the answer for a mathematical expression '
        f'({count_questions + 1}/{COUNT_TOURS}): \n'
        f'{expression} = '
        )

    if answer == r'\x':
        break

    if answer == right_answer:
        print(
            random.choice(['Right!', 'Yes!', 'Congrats!', 'Wonderful!']),
            end='\n\n'
            ) 
        count_right_answers += 1

    else:
        print(
            random.choice(['Sorry...', 'Oh, no...', 'Maybe another time...']),
            f'Correct answer: {right_answer} ',
            end='\n\n'
            ) 
    
    count_questions += 1 

else:
    print(f"That's all! You got {count_right_answers} point(s)!", end='\n\n')  