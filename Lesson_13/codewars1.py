import re
user_str = input()


def func(string):
    numbers = []
    number_str = '0'
    for char in string:
        if char.isdigit():
            number_str += char
        else:
            numbers.append(int(number_str))
            number_str = '0'

    numbers.append(int(number_str))
    return max(numbers)


def func2(string):
    return max(map(int, re.findall(r"(\d+)", string)))

print(func(user_str))
print(func2(user_str))
