"""Контекстні менеджери"""
import sqlite3


DB_FILE = 'tutorial.db'


class DbExecutor:
    """Класс для створення запиту до бази даних"""
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)

    def __enter__(self):
        return self

    def execute(self, statement):
        cursor = self.connection.cursor()
        cursor.execute(statement)
        self.connection.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

# def execute(statement):
# # Переписано через клас для реалізації можливості роботи з базою даних
# # через контекстний менеджер with (для гарантованого закриття підключення до бази)
# # Поганий приклад - працювати з базою даних можна через контекстний менеджер базово
#     """Запит до бази даних"""
#     connection = sqlite3.connect(DB_FILE)
#     cursor = connection.cursor()
#     cursor.execute(statement)
#     connection.commit()
#     connection.close()


with DbExecutor() as db_executor:
    db_executor.execute('CREATE TABLE movie(title, year, score)')