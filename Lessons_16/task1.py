"""Task 1 - School
Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another
one called Teacher. Try to find as many methods and attributes as
you can which belong to different classes, and keep in mind which are
common and which are not. For example, the name should be a Person
attribute, while salary should only be available to the teacher."""


class Person:
    """Basic person object"""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def talk(self):
        """Print greeting string"""
        print(f"Hello! I'm {self}")

    def __str__(self):
        return f"{self.name}, email: {self.email}"


class Student(Person):
    """Student object based on class Person"""

    def __init__(self, course, group, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course = course
        self.rating = 0
        self.group = group
        self.subjects = set()

    def add_subjects(self, subjects_list):
        """Add subject in subject set"""
        for sub in subjects_list:
            self.subjects.add(sub)

    def delete_subject(self, subject):
        """Remove subject from subject set"""
        self.subjects.remove(subject)

    def show_subjects(self):
        """Print student subjects"""
        print(", ".join(self.subjects))

    def set_rating(self, rating):
        """Setting student rating"""
        self.rating = rating

    def show_rating(self):
        """Print student rating"""
        print(self.rating)

    def __str__(self):
        return f"{self.name}, course: {self.course}, rating: {self.rating}"


class Teacher(Person):
    """Teacher object based on class Person"""

    def __init__(self, specialization, *args, salary=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary = salary
        self.specialization = specialization
        self.schedule = {
            "Monday": {},
            "Tuesday": {},
            "Wednesday": {},
            "Thursday": {},
            "Friday": {},
            "Saturday": {},
        }

    def add_schedule_entry(self, week_day, time, group, room):
        """Add new entry in schedule"""
        if time not in self.schedule[week_day]:
            self.schedule[week_day][time] = {"group": group, "class": room}
            return self.schedule[week_day][time]

        print("Error! Schedule already exist entry for this date and time")
        return None

    def delete_schedule_entry(self, week_day, time):
        """Remove entry from schedule"""
        if time in self.schedule[week_day]:
            entry = self.schedule[week_day][time]
            del self.schedule[week_day][time]
            return entry
        print("Error! Schedule not exist entry for this date and time")
        return None

    def show_schedule(self, week_day=None):
        """Return all entries in schedule"""
        return self.schedule[week_day] if week_day else self.schedule

    def __str__(self):
        return f"{self.name}, specialization: {self.specialization}"


print("Student:")
student = Student(
    "International relationship",
    "3C",
    "Luke Skywalker",
    "luke.skywalker@mail.com",
)
print(student)

print("\nRating after setting:")
student.set_rating(4.9)
student.show_rating()

student.add_subjects(["Economics", "Geography", "Psychology", "Philosophy"])
print("\nSubjects list after adding:")
student.show_subjects()

student.delete_subject("Psychology")
print("\nSubjects list after deleting 'Psychology':")
student.show_subjects()

print("\nGreeting:")
student.talk()

print("______________")

print("Teacher:")
teacher = Teacher("Jediism", "Obi-Wan Kenobi", "ben.kenobi@mail.com", salary=2500)
print(teacher)

teacher.add_schedule_entry("Monday", "19:00", "3C", 415)
teacher.add_schedule_entry("Thursday", "15:05", "2B", 405)
teacher.add_schedule_entry("Saturday", "11:10", "2A", 102)

print("\nSchedule after adding:")
print(teacher.show_schedule())

teacher.delete_schedule_entry("Monday", "19:00")
print("\nSchedule after deleting:")
print(teacher.show_schedule())

print("\nGreeting:")
teacher.talk()
