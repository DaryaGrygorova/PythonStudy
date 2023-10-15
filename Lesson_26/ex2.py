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

def my_hash_2(key_2: str):
    result = 1
    max_int = 32
    for symbol in key_2:
        result = (result * max_int + ord(symbol)) % 100
    return result


class MyDict:
    def __init__(self):
        self.storage = [[[None, None]]] * 100

    def get_by_key(self, my_key):
        index = my_hash(my_key)
        result = self.storage[index]
        if len(result) > 1:
            for key, value in result:
                if key == my_key:
                    return value
        return result[0][1]

    def save_value_by_key(self, my_key, value):
        index = my_hash(my_key)
        result = self.storage[index]
        if len(result) > 1:
            for ind, val in enumerate(result):
                if val.key == my_key:
                    self.storage[index][ind][1] = value
        self.storage[index] = [[my_key, value]]


my_custom_dict = MyDict()

my_custom_dict.save_value_by_key("one", 1)
my_custom_dict.save_value_by_key("two", 2)
my_custom_dict.save_value_by_key("two", 6)

print(my_custom_dict.get_by_key('two'))
