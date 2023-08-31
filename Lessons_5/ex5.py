# new_dict = {key_exp: value_exp for key, value in iterable [if expression]}
my_dict = {key: None for key in range(10)}
print(my_dict)

some_dictionary = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
}

new_dict = {value: key for key, value in some_dictionary.items()}
print(new_dict)