# Task 2 - Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial
# lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random

LIST_LENGTH = 10
first_list = []
second_list = []
third_list = []

while len(first_list) < LIST_LENGTH:
    first_list.append(random.randint(0, 10))
    second_list.append(random.randint(0, 10))
else:
    third_list = list(set(first_list).intersection(set(second_list)))

# An alternative way to compare lists without set() and for loop
# i = 0
# while i < LIST_LENGTH:
#     if first_list[i] in second_list and first_list[i] not in third_list:
#         third_list.append(first_list[i])
#     i += 1

print('First list:', first_list)
print('Second list:', second_list)
print('Comparative list:', third_list)
