"""
Reads file myfile.txt from directory "src" and prints its contents.
"""

with open('src\\myfile.txt', 'r', encoding="UTF-8") as file_obj:
    print(file_obj.read())
