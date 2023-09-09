"""
read imported file
"""

from ex2 import file_path

with open(file_path, 'r', encoding="UTF-8") as file_obj:
    print(file_obj.readlines())
