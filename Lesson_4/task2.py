# Task 2 - The birthday greeting program.
# Write a program that takes your name as input, and then your age
# as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”   

user_name = input("Please enter your name: ")
user_age = input("Please enter your age: ")

while not user_age:
    user_age = input("Please enter your age: ")

if user_age.isdigit():
    print(
        f"Hello {user_name.capitalize()}, on your next birthday"
        f" you’ll be {int(user_age) + 1} years"
        )
else:
    print('The age entry must contain only numbers!') 