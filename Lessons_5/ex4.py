# new_list = {expression_containing_item for item in iterable [if expression]}
some_list = [
    "Mango",
    "Apple",
    "Orange",
    "Kiwifruit",
    "Grape",
    "Banana",
    "Cherry",
    "Watermelon",
    "Pineapple",
    "Apricot",
    "Strawberry",
    "Avocado",
    "Peach",
    "Grapefruit",
    "Papaya",
    "Lemon",
    "Pear",
    "Blueberry",
    "Plum",
    "Pomegranate",
    "Blackberry",
    "Raspberry",
    "Guava",
    "Lime",
]

new_list = [item.lower() for item in some_list if 'a' in item.lower()]
# new_list = [item.lower() for item in some_list if 'a' in item or 'A' in item]
print(new_list)

def some_func():
    print('some_func')

some_func()