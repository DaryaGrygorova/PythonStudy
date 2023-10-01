"""Task 1
Create your own implementation of a built-in function enumerate,
named 'with_index', which takes two parameters: 'iterable' and
'start', default is 0.
Tips: see the documentation for the enumerate function
"""


class MyEnumerate:
    """Create custom enumerate object"""

    def __init__(self, iterable, start=0):
        self.index = 0
        self.start = start
        self.iterable = iterable or []

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.iterable):
            raise StopIteration
        res = (self.index + self.start, self.iterable[self.index])
        self.index += 1
        return res


def with_index(iterable, start):
    """Custom enumerate function"""
    return MyEnumerate(iterable, start)


test_list = [1, 2, 3, 4, 5, 6]
my_enumerate_arr = []
enumerate_arr = []

for index, item in with_index(test_list, 2):
    my_enumerate_arr.append((index, item))

for index, item in enumerate(test_list, 2):
    enumerate_arr.append((index, item))

assert my_enumerate_arr == enumerate_arr
