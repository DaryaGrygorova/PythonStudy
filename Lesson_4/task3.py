# Task 3 - Words combination
# Create a program that reads an input string and then creates 
# and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should
# print 5 random strings(words) that combine characters 
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)

import random

print(
    "This program creates and prints 5 random strings(words)\n"
    "that combine characters of the input string.\n"
    r"For exit enter '\x'",
    end ="\n\n"
    )

def create_new_str(string):
    new_str = "".join(random.sample(string, k=len(string)))
    return new_str

while True:
    user_input = input("Please input string: ")

    if user_input == r'\x':
        break

    if len(user_input) >= 25:
        print(
            'Your string is too long! '
            'Please enter a string of up to 25 characters!\n'
            )
        continue

    print(
        create_new_str(user_input),
        create_new_str(user_input),
        create_new_str(user_input),
        create_new_str(user_input),
        create_new_str(user_input),
        sep=', ',
        end='\n\n'
        )