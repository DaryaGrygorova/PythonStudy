# Task 1 - The greatest number
# Write a Python program to get the largest number from a list of random numbers
# with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random

LIST_LENGTH = 10
new_list = []

# An alternative way to create a list of random numbers with the length of 10
# new_list = random.sample(range(1, 100), k=LIST_LENGTH)

while len(new_list) < LIST_LENGTH:
    new_list.append(random.randint(0, 100))
else:
    largest_num = new_list[0]

    i = 0
    while i < LIST_LENGTH - 1:
        i += 1                          # елемент під індексом 0 не потребує порівняння
        if new_list[i] > largest_num:
            largest_num = new_list[i]
        else:
            continue
    else:
        print("List: ", new_list, '\n', 'Largest number: ', largest_num, sep='')
