"""Task 4 - Custom exception
Create your custom exception named 'CustomException',
you can inherit from base Exception class, but extend its functionality
to log every error message to a file named 'logs.txt'.

Tips: Use __init__ method to extend functionality for saving messages to file
"""


class CustomException(Exception):
    """Custom Error object"""

    def __init__(self, message, log_path="error_log.txt"):
        super()
        self.message = message
        self.loger(log_path)

    def loger(self, log_path):
        """Log error message in file"""
        with open(log_path, "a", encoding="UTF-8") as log_file:
            log_file.write(self.message + "\n")

    @staticmethod
    def read_error_log(log_path="error_log.txt"):
        """Read error log from file"""
        try:
            with open(log_path, "r", encoding="UTF-8") as log_file:
                print(log_file.read())
        except FileNotFoundError:
            print(f'Log file "{log_path}" not found')


try:
    raise CustomException("My custom error")
except CustomException as exception:
    CustomException.read_error_log()
