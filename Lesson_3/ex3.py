my_dict = {"one": [bool('str'), {'cow': 'boy', "moon": 'sun'}]}

# виводимо "sun"
print(my_dict['one'][1]["moon"])
# print(my_dict.one[1]["moon"])  -  AttributeError: 'dict' object has no attribute 'one'