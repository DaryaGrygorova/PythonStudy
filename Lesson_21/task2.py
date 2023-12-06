"""
Task 2 - Writing tests for context manager
Take your implementation of the context manager class from Task 1
and write tests for it. Try to cover as many use cases as you can,
positive ones when a file exists and everything works as designed.
And also, write tests when your class raises errors |or you
have errors in the runtime context suite.
"""
import os
import unittest
from Lesson_21.task1 import MyFileContextManager


class MyFileContextManagerTest(unittest.TestCase):
    """Tests for My_File_Context_Manager class"""

    def setUp(self):
        self.context_manager = MyFileContextManager

    def tearDown(self):
        """Remove test data"""
        if os.path.exists("my_file_context_manager_log.txt"):
            os.remove("my_file_context_manager_log.txt")
        if os.path.exists("test.txt"):
            os.remove("test.txt")
        self.context_manager.reset_counter()

    def open_file_successful(self, file_name, mode="r"):
        """Open file with MyFileContextManager"""
        with self.context_manager(file_name, mode) as _:
            pass

    def open_file_with_file_not_exist_error(self, file_name="__test", mode="r"):
        """Open non-existent file with MyFileContextManager"""
        try:
            self.open_file_successful(file_name, mode)
        except FileNotFoundError:
            pass

    def open_file_with_processing_error(self, file_name="test.txt", mode="a"):
        """Open file with processing error"""
        try:
            with self.context_manager(file_name, mode) as file_obj:
                file_obj.write("Line 3")
                raise ChildProcessError
        except ChildProcessError:
            pass

    def test_open_to_read_non_existent_file(self):
        """Checking if FileNotFoundError occurs when opening a non-existent file"""
        self.assertRaises(FileNotFoundError, self.open_file_successful, "test.txt", "r")

    def test_open_to_write_non_existent_file(self):
        """Checking new file creation when opening a non-existent file"""
        with self.context_manager("test.txt", "w") as _:
            self.assertTrue(os.path.exists("test.txt"))

    def test_write_append_and_read_text_in_file(self):
        """Checking new file creation when opening a non-existent file"""
        test_text = "Hello, world!!!"
        with self.context_manager("test.txt", "w") as file_obj:
            file_obj.write(test_text)
        with self.context_manager("test.txt", "a") as file_obj:
            file_obj.write(test_text)
            file_obj.write(test_text)
        with self.context_manager("test.txt", "r") as file_obj:
            self.assertEqual(file_obj.read(), test_text * 3)

    def test_counter(self):
        """Test count of call of MyFileContextManager.__enter__ method"""
        with self.context_manager("test.txt", "w") as file_obj:
            file_obj.write("Line 1")
            file_obj.write("Line 2")
        self.assertEqual(self.context_manager.get_counter(), 1)

        self.open_file_successful("test.txt")
        self.assertEqual(self.context_manager.get_counter(), 2)

        self.open_file_with_file_not_exist_error()
        self.assertEqual(self.context_manager.get_counter(), 3)

        self.open_file_with_processing_error()
        self.assertEqual(self.context_manager.get_counter(), 4)

    def test_logger(self):
        """Test logger of call of MyFileContextManager"""
        # 2 new lines are expected to appear in the log if the file was opened and closed
        with self.context_manager("test.txt", "w") as file_obj:
            file_obj.write("Line 1")
            file_obj.write("Line 2")
        with open(self.context_manager.get_log_name(), encoding="UTF-8") as log_file:
            self.assertEqual(len(log_file.readlines()), 2)

        # 1 new line is expected to appear in the log if the file to be opened does not exist
        self.open_file_with_file_not_exist_error()
        with open(self.context_manager.get_log_name(), encoding="UTF-8") as log_file:
            self.assertEqual(len(log_file.readlines()), 3)

        # 2 new lines are expected to appear in the log if the file was opened and closed
        self.open_file_with_processing_error("test.txt")
        with open(self.context_manager.get_log_name(), encoding="UTF-8") as log_file:
            self.assertEqual(len(log_file.readlines()), 5)

    def test_close_file(self):
        """Checking file closing"""
        # Successful case
        with self.context_manager("test.txt", "w") as file_obj:
            file_obj.write("Line 1")
            file_obj.write("Line 2")
            self.assertFalse(file_obj.closed)
        self.assertTrue(file_obj.closed)

        # Case with error
        try:
            with self.context_manager("test.txt", "a") as other_file_obj:
                other_file_obj.write("Line 3")
                self.assertFalse(other_file_obj.closed)
                raise ChildProcessError
        except ChildProcessError:
            pass
        self.assertTrue(other_file_obj.closed)


if __name__ == "__main__":
    unittest.main()
