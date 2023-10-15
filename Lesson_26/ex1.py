"""
Hash algorithm properties:
1. "Avalanche effect" - the tiniest change in incoming data changes the result completely
2. The possibility of each resulting checksum (hash) is the same to any other
3. You can not recreate the original contents from the checksum easily
"""
import ctypes
import random
from string import ascii_letters
from matplotlib import pyplot


def my_hash(key: str):
    factor_1 = len(key) or 1
    factor_2 = sum(ord(symbol) for symbol in key)
    factor_3 = sum(ord(symbol) for symbol in ctypes.cast(id(key), ctypes.py_object).value)

    result = (factor_2**2)/(factor_1+factor_3)

    return int(result%100)


def gen_random_string():
    result_len = random.randint(0, 10)
    all_characters = ascii_letters + '0123456789'

    return ''.join([random.choice(all_characters) for _ in range(result_len)])


result_range = range(101)
data = dict.fromkeys(result_range, 0)
for _ in range(1000):
    new_key = my_hash(gen_random_string())
    data[new_key] = data[new_key] + 1


names = list(data.keys())
values = list(data.values())

pyplot.bar(range(len(data)), values, tick_label=names)
pyplot.show()
