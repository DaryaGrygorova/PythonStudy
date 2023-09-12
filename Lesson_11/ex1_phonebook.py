"""
Phonebook
"""

import sys
import os

print(sys.argv)

current_dir = os.path.dirname(os.path.realpath(__file__))
data_file_path = os.path.join(current_dir, 'src', sys.argv[1] + '.json')


with open(data_file_path, 'a', encoding='UTF-8') as phonebook_file:
    print(phonebook_file)


DATA = {
   1: {"Name": "Petro Ivanov", "Location": "Kiiv"},
}

PHONEBOOK = {
    "+3809755555555": DATA[1],      # Для виключення дублювання даних
    "+3809766666666": DATA[1],
}


input()
