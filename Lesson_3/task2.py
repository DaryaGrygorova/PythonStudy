# Task 2 - The valid phone number program.
# Make a program that checks if a string is in the right format 
# for a phone number. The program should check that the string 
# contains only numerical characters and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string evaluation.

print(
    'This program checks if the string has the correct format '
    'for the phone number.\nThe string must contain only numeric '
    'characters\nand be no more than 10 characters long.' 
    )

while True:
    phone_number = input(
        "Please enter a number. For exit enter " r"'\x'" "\n"
        )

    if phone_number == r'\x':
        break

    if len(phone_number) >= 10:
        print(
            'Error! String must be no more than 10 characters long!', 
            end='\n\n'
            ) 

    elif len(phone_number) < 5:
        print('Error! String is too short!', end='\n\n') 

    elif not phone_number.isdigit():
        print(
            'Invalid number! '
            'Phone number must contain only numeric characters!',
            end='\n\n'
            )
        break
    else:
        print('Phone number is valid!', end='\n\n')  