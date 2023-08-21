# Task 4 - The name check.
# Write a program that has a variable with your name stored (in lowercase) 
# and then asks for your name as input. The program should check 
# if your input is equal to the stored name even if the given name has 
# another case, e.g., if your input is “Anton” and the stored name is “anton”, 
# it should return True.

print(
    "This program checks if your name matches the saved one." r"'\x'" "\n" 
    )

NAME="darya"

while True:
    user_name = input("Please enter your name: ")

    if user_name == r'\x':
        break

    if user_name.lower() == NAME:
        print(
            f'Hello, {NAME.capitalize()}! Nice to meet you!', end='\n\n') 
    else:
        print('Excuse me, do I know you?', end='\n\n') 