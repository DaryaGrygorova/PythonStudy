"""
Write tests for the Phonebook application, which you have implemented in module 1.
Design tests for this solution and write tests using unittest library
"""
import json
import unittest
import os
from testing_phone_book import PhoneBook


class PhonebookTest(unittest.TestCase):
    """Tests for class PhoneBook methods"""

    def setUp(self):
        # Prepare environment
        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.file_path = os.path.join(current_dir, "phonebookTest.json")
        self.temp_path = os.path.join(current_dir, "temp.json")
        self.mock_path = os.path.join(current_dir, "mock", "phonebook_mock_data.json")
        with open(self.mock_path, "r", encoding="UTF_8") as mock_file:
            self.mock_data = json.load(mock_file)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="UTF-8") as file:
                file.write("{}")

        self.phone_book = PhoneBook(self.file_path, self.temp_path, self.mock_path)
        self.new_entry = {
            "first_name": "Sarah",
            "last_name": "Connor",
            "location": "Los Angeles, California",
            "phone": "+1-213-978-2222",
        }

    def tearDown(self):
        """Remove test data"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.temp_path):
            os.remove(self.temp_path)

    def test_add(self):
        """Test add function"""
        self.phone_book.add(self.new_entry)
        new_contact = {
            self.new_entry["phone"]: {
                "first_name": self.new_entry["first_name"],
                "last_name": self.new_entry["last_name"],
                "location": self.new_entry["location"],
            }
        }
        base = self.phone_book.open_file()
        self.assertEqual(base, new_contact)

    def test_save_phonebook_to_file(self):
        """Test save_phonebook_to_file function"""
        self.phone_book.save_phonebook_to_file(self.mock_data)
        base = self.phone_book.open_file()
        self.assertEqual(base, self.mock_data)

    def test_search_by_phone(self):
        """Test search_by function (key 'phone')"""
        self.phone_book.backup_phonebook(self.mock_path)

        # Search by phone (number not exist in phone book)
        result = self.phone_book.search_by('phone', "+1-213-978-5555")
        self.assertEqual(result, None)

        # Search by phone (number exist in phone book)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('phone', self.new_entry['phone'])
        self.assertEqual(result, [self.new_entry])

    def test_search_by_first_name(self):
        """Test search_by function (key 'first_name')"""
        self.phone_book.backup_phonebook(self.mock_path)
        # Search by first name (first name not exist in phone book)
        result = self.phone_book.search_by('first_name', "Sarah")
        self.assertEqual(result, None)

        # Search by first name (first name exist in phone book)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('first_name', "Sarah")
        self.assertEqual(result, [self.new_entry])

    def test_search_by_last_name(self):
        """Test search_by function (key 'last_name')"""
        self.phone_book.backup_phonebook(self.mock_path)
        # Search by last name (last name not exist in phone book)
        result = self.phone_book.search_by('last_name', "Connor")
        self.assertEqual(result, None)

        # Search by last name (last name exist in phone book)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('last_name', "Connor")
        self.assertEqual(result, [self.new_entry])

    def test_search_by_full_name(self):
        """Test search_by function (key 'full_name')"""
        self.phone_book.backup_phonebook(self.mock_path)
        # Search by full name (full name not exist in phone book)
        result = self.phone_book.search_by('full_name', "Sarah Connor")
        self.assertEqual(result, None)

        # Search by full name (full name exist in phone book)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('full_name', "Sarah Connor")
        self.assertEqual(result, [self.new_entry])

    def test_search_by_location(self):
        """Test search_by function (key 'location')"""
        self.phone_book.backup_phonebook(self.mock_path)
        # Search by location (location not exist in phone book)
        result = self.phone_book.search_by('location', "Los Angeles, California")
        self.assertEqual(result, None)

        # Search by location (location exist in phone book)
        self.phone_book.add(self.new_entry)
        result = self.phone_book.search_by('location', "Los Angeles, California")
        self.assertEqual(result, [self.new_entry])

    def test_delete_by_phone(self):
        """Test delete_by_phone function"""
        self.phone_book.backup_phonebook(self.mock_path)

        # Deleting no exist contact
        self.phone_book.delete_by_phone("+1-213-978-5555")
        base = self.phone_book.open_file()
        self.assertEqual(base, self.mock_data)

        # Deleting exist contact
        self.phone_book.add(self.new_entry)
        self.phone_book.delete_by_phone(self.new_entry["phone"])
        base = self.phone_book.open_file()
        self.assertEqual(base, self.mock_data)

    def test_update_by_phone(self):
        """Test update_by_phone function"""
        self.phone_book.add(self.new_entry)
        new_data = {
            "first_name": self.new_entry["first_name"],
            "last_name": "Reese",
            "location": self.new_entry["location"],
        }
        self.phone_book.update_by_phone(self.new_entry["phone"], new_data)
        new_contact = {self.new_entry["phone"]: new_data}

        base = self.phone_book.open_file()
        self.assertEqual(base, new_contact)

    def test_backup_phonebook(self):
        """Test creation and saving backup file in phonebook"""
        self.phone_book.save_phonebook_to_file(self.mock_data)
        self.phone_book.create_backup_file()

        self.phone_book.save_phonebook_to_file({})

        base = self.phone_book.open_file()
        self.assertEqual(base, {})

        self.phone_book.backup_phonebook(self.temp_path)
        base = self.phone_book.open_file()
        self.assertEqual(base, self.mock_data)


if __name__ == "__main__":
    unittest.main()
