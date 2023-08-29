# Task 1 - String manipulation
# Write a Python program to get a string made of the first 2 
# and the last 2 chars from a given string. If the string length is less than 2,
# return instead of the empty string.

# Sample String: 'helloworld'
# Expected Result : 'held'
# Sample String: 'my'
# Expected Result : 'mymy'
# Sample String: 'x'
# Expected Result: Empty String

# Tips:
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string 
# and negative indexing to get the last characters

print(
    'This program creates a string from the first 2 ' 
    'and the last 2 chars of a given string.'
    )

while True:
    string = input(
        "Please enter a string (at least 2 characters). "
        "For exit enter " r"'\x'" "\n"
        )

    if string == r'\x':
        break

    if len(string) >= 2:
        new_string = string[0:2:] + string[-2::]
        print(new_string, end='\n\n')  
    else:
        print('', end='\n\n')    