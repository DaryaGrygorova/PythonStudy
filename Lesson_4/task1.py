# Task 1 - The Guessing Game.
# Write a program that generates a random number 
# between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random

print(r"Welcome to Guess the Number. For exit enter '\x'" "\n")

while True:
    random_number = random.randint(1, 10)
    user_input = input("Please input number between 1 and 10: ")

    if user_input == r'\x':
        break

    if user_input.isdigit():
        if int(user_input) > 10 or int(user_input) < 1:
            print("Please input number between 1 and 10: ")
        else:
            if int(user_input) == random_number:
                print("You guessed, congrats!\n")
            else:
                print(f"Sorry, you didn't guess! My number: {random_number}\n")
    else:
        print("It's not a number!")