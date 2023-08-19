import random

random_number = random.randint(1, 10)
user_input = input("Please input number between 1 and 10: ")

# todo: validate user input
if int(user_input) > 10 or int(user_input) < 1:
    print("Please input number between 1 and 10: ")
else:
    if int(user_input) == random_number:
        print("You guessed? congrats!")
    else:
        print(f"Sorry, you didn't guess! My number: {random_number}")
