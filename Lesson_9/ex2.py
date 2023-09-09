""" """

LIST_1 = [1, 2, 3]
LIST_2 = [1, 2, 3]

print(LIST_1 == LIST_2) # True - порівняння елементів списку по-порядку
print(LIST_1 is LIST_2) # False - різні id
print(id(LIST_1) == id(LIST_2)) # False
print(id(LIST_1) is id(LIST_2)) # False

print("-----------------")

LIST_2 = LIST_1 # присвоєння за посиланням

print(LIST_1 == LIST_2)
print(LIST_1 is LIST_2) # True - однакові id
