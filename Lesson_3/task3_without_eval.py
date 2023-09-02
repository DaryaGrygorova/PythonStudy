""" Task 3 - The math quiz program.
Write a program that asks the answer for a
mathematical expression, checks whether the user is right or wrong,
and then responds with a message accordingly.
"""

import random

print(r"Welcome to math quiz!!! For exit enter '\x'")

COUNT_TOURS = 5
COUNT_QUESTIONS = 0
COUNT_RIGHT_ANSWERS = 0


def create_expression():
    """"Function return expression and its result"""
    operand_1 = random.randrange(1, 11)
    operand_2 = random.randrange(1, 11)
    operator = random.choice(["*", "//", "+", "-"])

    math_expression = f"{operand_1} {operator} {operand_2}"
    expression_result = ""

    match operator:
        case "*":
            expression_result = str(operand_1 * operand_2)
        case "//":
            expression_result = str(operand_1 // operand_2)
        case "+":
            expression_result = str(operand_1 + operand_2)
        case "-":
            expression_result = str(operand_1 - operand_2)

    return math_expression, expression_result


while COUNT_QUESTIONS < COUNT_TOURS:
    expression, right_answer = create_expression()

    answer = input(
        "Please enter the answer for a mathematical expression "
        f"({COUNT_QUESTIONS + 1}/{COUNT_TOURS}): \n"
        f"{expression} = "
    )

    if answer == r"\x":
        break

    if answer == right_answer:
        print(random.choice(["Right!", "Yes!", "Congrats!", "Wonderful!"]), end="\n\n")
        COUNT_RIGHT_ANSWERS += 1

    else:
        print(
            random.choice(["Sorry...", "Oh, no...", "Maybe another time..."]),
            f"Correct answer: {right_answer} ",
            end="\n\n",
        )

    COUNT_QUESTIONS += 1

else:
    print(f"That's all! You got {COUNT_RIGHT_ANSWERS} point(s)!", end="\n\n")
