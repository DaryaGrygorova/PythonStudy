"""
Phonebook
"""
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_file_path", help="Phonebook file path")
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))
data_file_path = os.path.join(current_dir, 'src', args.data_file_path + '.json')

#  Need to add initialization for empty phonebook file
#  if not os.path.exist(data_file_path):
#     with open(data_file_path, 'w') as file:
#         file.write({})


DATA = {
   1: {"Name": "Petro Ivanov", "Location": "Carolina"},
   2: {"Name": "Petro Ivanov", "Location": "Texas"},
   3: {"Name": "Petya Ivanov", "Location": "Texas"},
}

PHONES = {
    "+3809755555555": 1,
    "+3809766666666": 1,
    "+3809777777777": 2,
    "+3809788888888": 3
}

PHONEBOOK = {phone: DATA[value] for phone, value in PHONES.items()}

with open(data_file_path, 'a', encoding="UTF-8") as phonebook_file:
    json.dump(PHONEBOOK, phonebook_file, indent=4)

with open(data_file_path, 'r', encoding="UTF-8") as phonebook_file:
    print(json.load(phonebook_file))      # save data in file

input()
