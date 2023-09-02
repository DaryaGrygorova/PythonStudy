"""
Task 4
Create a list with the names of the days of the week.
In one line (or as usual) create a dictionary of the form: {1: "Monday", 2:...
Also in one line (or as usual) create a reverse dictionary {"Monday": 1,...
"""

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

first_week_dict = {(i + 1): day for i, day in enumerate(days)}
print(first_week_dict)

second_week_dict = {day: (i + 1) for i, day in enumerate(days)}
print(second_week_dict)
