""" """

import os

# отримуємо абсолютний шлях до папки з файлом
working_directory = os.path.dirname(os.path.realpath(__file__))

# отримуємо абсолютний шлях до файлу з урахуванням особливостей системи
# яка може використовувати як прямий так і зворотній слеш
# при формуванні шляхів до файлів
file_path = os.path.join(working_directory, 'temp.txt')

# Для вірішення цієї проблеми використовується контекстний менеджер
with open(file_path, 'a', encoding="UTF-8") as file_obj:
    file_obj.write(input("Type something: "))
