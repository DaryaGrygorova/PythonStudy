"""Task 3
Create your own implementation of an iterable, which could be used
inside for-in loop. Also, add logic for retrieving elements using
square brackets syntax.
"""


class MyIterable:
    """Create custom iterable object"""
    def __init__(self, init_object):
        self.index = 0
        self._iterable = init_object

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self._iterable):
            raise StopIteration
        res = self._iterable[self.index]
        self.index += 1
        return res

    def __getitem__(self, index):
        return self._iterable[index]

    def __len__(self):
        return len(self._iterable)


test_object = "test_string"
char_list = []
char_list_1 = []
char_list_2 = []

my_iterable_object = MyIterable(test_object)

for el in my_iterable_object:
    char_list.append(el)

for _, value in enumerate(my_iterable_object):
    char_list_1.append(value)

for i in range(0, len(my_iterable_object)):
    char_list_2.append(my_iterable_object[i])

assert list(my_iterable_object) == char_list
assert list(my_iterable_object) == char_list_1
assert list(my_iterable_object) == char_list_2
