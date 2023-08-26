sqr_list = []

for number in range(1, 11):
    if number % 3 != 0:
        sqr_list.append(number**2)
    else:
       sqr_list.append(number**3)
print(sqr_list)

# еквівалентний запис
sqr_list = [number**2 if number % 3 != 0 else number**3 for number in range(1, 11) ]
print(sqr_list)

# Присвоєння значення по умові
test = True
new_var = 1 if test else 100
print(new_var)

test = False
new_var = 1 if test else 100
print(new_var)
