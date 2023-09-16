"""
Phonebook
"""
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="Name of Phonebook")
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(current_dir, 'src', args.file_name + '.json')

# Initialization for empty phonebook file
print(os.path.exists(file_name))
if not os.path.exists(file_name):
    with open(file_name, 'w', encoding="UTF-8") as file:
        print('create new file')
        file.write('{"Phonebook_name": ' + f'"{args.file_name}"' + '}')


def show_all():
    """ Show all entries"""
    with open(file_name, 'r', encoding="UTF-8") as book:
        print(book.read())


def add():
    """Add new entries"""
    print('Please, enter the details for creating new contact')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    phone_number = input('Enter phone number: ')
    location = input('Enter city or state: ')

    # Need to add check if this contact exists in phonebook
    with open(file_name, 'r') as book_file:
        phonebook = json.load(book_file)
        phonebook[f'{first_name} {last_name}'] = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'location': location
        }

# У разі винекнення помилки під час запису файл file_name буде перезаписаний на пустий
# для уникнення втрати данних можна попередній варіант файлу записувати в тимчасовий файл
# та перезаписувати з нього основний у разі пимилки
    temp_file_path = os.path.join(current_dir, 'src', 'temp.json')
    os.replace(file_name, temp_file_path)

    try:
        with open(file_name, 'w') as book_file:
            raise ValueError
            json.dump(phonebook, book_file, indent=4)
    except ValueError:
        print("Error")
        with open(temp_file_path, 'r') as temp_file:
            temp_data = json.load(temp_file)
        with open(file_name, 'w') as book_file:
            json.dump(temp_data, book_file, indent=4)


add()
show_all()
input()