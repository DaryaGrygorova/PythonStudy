"""
Phonebook
"""
import json
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="Name of Phonebook")
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(current_dir, args.file_name + ".json")
temp_file = os.path.join(current_dir, "src", "temp.json")

# Initialization for empty phonebook file
if not os.path.exists(file_name):
    input_code = input(
        f"File with name '{args.file_name}' not found!\n"
        "Do you want to create new file? (y/n)"
    )
    if not input_code.lower() == "y":
        sys.exit()

    with open(file_name, "w", encoding="UTF-8") as file:
        file.write("{}")


def open_file():
    """Open phonebook file to read"""
    try:
        with open(file_name, "r", encoding="UTF_8") as book_file:
            return json.load(book_file)
    except FileNotFoundError:
        print(f'Error! File with name "{args.file_name}" not found!')
    return None


def create_backup_file():
    """Create backup file"""
    os.replace(file_name, temp_file)


def backup_phonebook(backup_file=None):
    """Rewrite phonebook file from backup file"""
    try:
        with open(backup_file, "r", encoding="UTF_8") as file_obj:
            temp_data = json.load(file_obj)
        with open(file_name, "w", encoding="UTF_8") as book_file:
            json.dump(temp_data, book_file, indent=4)
    except FileNotFoundError:
        print("Error: Backup file not exist")


def save_phonebook_to_file(phonebook):
    """Convert object phonebook to json format and save it to file"""
    try:
        with open(file_name, "w", encoding="UTF_8") as book_file:
            json.dump(phonebook, book_file, indent=4)
    except Exception:
        print("Rewrite error!")
        backup_phonebook(temp_file)


def show_all():
    """Show all entries in phonebook"""
    try:
        with open(file_name, "r", encoding="UTF_8") as book_file:
            print(book_file.read())
    except FileNotFoundError:
        print(f'Error! File with name "{args.file_name}" not found!')


def add():
    """
    Add new entries.
    Return True if operation completed successful, and False in another case.
    """
    print("Please, enter the details for creating new contact:")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    location = input("Enter city or state: ")

    phonebook = open_file()

    if phone in phonebook:
        print(f"Contact with phone number {phone} is already exist!")
        operation_code = input("Do you want to update this data? (y/n): ")
        if not operation_code == "y":
            return False

    # create new contact
    phonebook[f"{phone}"] = {
        "first_name": first_name,
        "last_name": last_name,
        "location": location,
    }

    # create backup file
    create_backup_file()

    # update phonebook
    save_phonebook_to_file(phonebook)

    return True


def search_by(key):
    """Search contact by key and its value"""
    phonebook = open_file()

    user_value = input(f"Search contact(s) by {key.replace('_', ' ')}: ")

    contacts = []

    match key:
        case "phone":
            if user_value not in phonebook:
                return None
            data = phonebook[user_value]
            data["phone"] = user_value
            contacts.append(data)
        case "full_name":
            for contact, data in phonebook.items():
                if (
                    user_value.lower()
                    == f"{data['first_name']} {data['last_name']}".lower()
                ):
                    data["phone"] = contact
                    contacts.append(data)
                continue
        case _:
            for contact, data in phonebook.items():
                if user_value.lower() == data[key].lower():
                    data["phone"] = contact
                    contacts.append(data)
                continue

    return json.dumps(contacts, indent=4) if len(contacts) > 0 else None


def update_by_phone():
    """
    Update a record for a given telephone number.
    Return True if operation completed successful, and False in another case.
    """
    phone = input("Enter phone number: ")
    phonebook = open_file()

    if phone not in phonebook:
        print(f"Contact with phone number {phone} not found.")
        operation_code = input("Do you want to add this contact as new? (y/n): ")
        if not operation_code == "y":
            return False

    print("Please, enter the details for updating contact:")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    location = input("Enter city or state: ")

    # update data
    phonebook[f"{phone}"] = {
        "first_name": first_name,
        "last_name": last_name,
        "location": location,
    }

    # create backup file
    create_backup_file()

    # update phonebook
    save_phonebook_to_file(phonebook)

    return True


def delete_by_phone():
    """
    Delete a record for a given telephone number
    Return True if operation completed successful, and False in another case.
    """
    phone = input("Enter phone number: ")
    phonebook = open_file()
    if phone not in phonebook:
        print(f"Contact with phone number {phone} not found!")
        return False
    del phonebook[phone]
    save_phonebook_to_file(phonebook)
    return True


def phonebook_ui():
    """Main function loop"""
    while True:
        print(
            "\n",
            "What do you want to do?",
            "1. Add contact",
            "2. Search by first name",
            "3. Search by last name",
            "4. Search by full name",
            "5. Search by phone number",
            "6. Search by location",
            "7. Update contact by phone number",
            "8. Delete contact by phone number",
            "9. Show all contacts in phonebook",
            "10. Backup phonebook from Mock_data",
            "Enter 'q' to quit",
            sep="\n",
        )
        operation_code = input("Enter the code: ")

        match operation_code:
            case "1":
                success = add()
                if success:
                    print("The Phonebook successfully updated!")
            case "2":
                print(search_by("first_name") or "Contact(s) not found!")
            case "3":
                print(search_by("last_name") or "Contact(s) not found!")
            case "4":
                print(search_by("full_name") or "Contact(s) not found!")
            case "5":
                print(search_by("phone") or "Contact(s) not found!")
            case "6":
                print(search_by("location") or "Contact(s) not found!")
            case "7":
                success = update_by_phone()
                if success:
                    print("The Phonebook successfully updated!")
            case "8":
                success = delete_by_phone()
                if success:
                    print("The contact successfully deleted!")
            case "9":
                show_all()
            case "10":
                backup_phonebook(
                    os.path.join(current_dir, "src/mock/phonebook_mock_data.json")
                )
                print("The Phonebook successfully updated!")
            case "q":
                sys.exit()
            case _:
                print("Unknown code. Try again")
                continue
        input("Press 'Enter' to continue.")

phonebook_ui()
