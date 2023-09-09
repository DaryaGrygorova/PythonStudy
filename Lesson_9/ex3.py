""" """

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# first_week_dict = {(i + 1): day for i, day in enumerate(days)}
first_week_dict = dict(enumerate(days, start=1))
print(first_week_dict)

# second_week_dict = {day: (i + 1) for i, day in enumerate(days)}
second_week_dict = {value: key + 1 for key, value in first_week_dict.items()}
print(second_week_dict)
