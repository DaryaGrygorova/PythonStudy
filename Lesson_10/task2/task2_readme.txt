Task 2 - Extend Phonebook application

Functionality of Phonebook application:
Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program

The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with
application, else raise an error. After the user exits, all data should be
saved to loaded JSON.

My note:
1. Additional functionality of app:
    - Show all contacts in phonebook
    - Rewrite phonebook from Mock_data

2. JSON-file format:
Object with phone numbers as keys and the rest of the contact data as values
For example:
{
"4121815445": {
        "first_name": "Patience",
        "last_name": "Battin",
        "location": "07065 Schlimgen Street"
    }
}