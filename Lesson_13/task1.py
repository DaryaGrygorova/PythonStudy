"""
Task 1
Write a Python program to detect the number of local variables declared in a function.
"""
import random


def count_variables(func_name):
    """Return the number of local variables declared in a function 'func_name'"""
    return func_name.__code__.co_nlocals


def square_func():
    """Returns list of the squares of the numbers from nums"""
    nums = [1, 2, -5, 26]
    res = [num**2 for num in nums]
    return res


def user_creator(user_name):
    """Returns user object with user_name"""
    name = user_name
    age = random.randint(18, 99)
    sex = random.choice(["male", "female"])
    pet = random.choice(["cat", "dog", "crow", "owl"])
    is_lucky = bool(sex == "male" and not pet == "cat") or bool(
        sex == "female" and pet == "cat" and age > 40
    )

    user = {"name": name, "age": age, "pet": pet, "is_lucky": is_lucky}

    return user


print(count_variables(square_func))  # 2 - [nums, res]
print(count_variables(user_creator))  # 7 - [user_name, user, name, age, pet, is_lucky]
