"""
Try/except
"""

""" """

import os

working_directory = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(working_directory, 'temp.txt')

try:
    file_obj = open(file_path, 'a', encoding="UTF-8")
except FileNotFoundError:
    print('File not exist')
else:
    file_obj.write(input("Type something: ")) # виконається, лише якщо відпрацює блок try
finally:
    print('done')
