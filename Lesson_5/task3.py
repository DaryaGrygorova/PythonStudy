# Task 3 - Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers
# from the list that are divisible by 7 but not a multiple of 5, and store them
# in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

my_list = list(range(1, 101))
new_list = []
i = 0
while i < len(my_list):
    if not my_list[i] % 7 and my_list[i] % 5:
        new_list.append(my_list[i])
    i += 1
else:
    print(
        'List of numbers from 1 to 100 that are '
        'divisible by 7 but not a multiple of 5: \n',
        new_list)

