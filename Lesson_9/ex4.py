"""
Задача - продублювати "компрехеншен" для new_list іншими способами
new_list = [day for nested_list in days_nested for day in nested_list]
"""

days_nested = [['Monday', 'Tuesday'], ['Wednesday', 'Thursday'], ['Friday', 'Saturday', 'Sunday']]

# first
new_list = []
for item in days_nested:
    for day in item:
        new_list.append(day)
print(new_list)

# second
new_list = []
for item in days_nested:
    new_list = [*new_list, *item]
print(new_list)

# third
new_list = []
for inner_list in days_nested:
    new_list += inner_list
print(new_list)

# forth
new_list = []
i = 0
while i < len(days_nested):
    new_list += days_nested[i]
    i += 1
print(new_list)
