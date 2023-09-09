"""IO - imput/output"""
import os

# отримуємо абсолютний шлях до папки з файлом
working_directory = os.path.dirname(os.path.realpath(__file__))

# отримуємо абсолютний шлях до файлу з урахуванням особливостей системи
# яка може використовувати як прямий так і зворотній слеш
# при формуванні шляхів до файлів
file_path = os.path.join(working_directory, 'temp.txt')

# після роботи з файлом його необхідно закрити,
# однак, якщо в блоці між відкриттям та закриттям станеться помилка
# файл не закриється
file_obj = open(file_path, 'w')
raise Exception
file_obj.close() # не спрацює

# Для вірішення цієї проблеми використовується контекстний менеджер
with open(file_path, 'r+', encoding="UTF-8") as file_obj:
    print(file_obj.readlines())
    raise Exception # перед "викиданням" помилки файл закриється
