"""Task 4
Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,
"""

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

first_week_dict = {(i + 1): day for i, day in enumerate(days)}
print(first_week_dict)

second_week_dict = {day: (i + 1) for i, day in enumerate(days)}
print(second_week_dict)
