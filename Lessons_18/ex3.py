"""Generators"""


class MyGenerator:
    """Custom Generator"""

    def __init__(self, end=5):
        self.index = 0
        self.end = end

    def __iter__(
        self,
    ):  # this method call when call method iter() on instance of MyIter
        self.index = 0
        return self  # return self, because we need call custom method next from instance of MyIter

    def __next__(self):
        if self.index == self.end:
            raise StopIteration
        self.index += 1
        return self.index - 1


my_generator = MyGenerator(5)  # instantiation

for item in my_generator:  # new_iterator_obj = iter(my_generator) == my.iter.__iter__()
    print(item)  # next(new_iterator_obj) == my_generator.__next__()

print("___________")
# for new_item in my_iter:
#     print(new_item)
# in details:
new_generator_obj = iter(my_generator)  # iter(my_generator) is equal my_generator.__iter__()
while True:
    try:
        index_inside_each_iteration = next(
            new_generator_obj
        )  # next(new_generator_obj) is equal new_generator_obj.__next__,
           # and it is equal my_generator.__iter__().__next__()
        # action inside iteration (line 23)
        print(index_inside_each_iteration)
    except StopIteration:
        # exit while-loop
        break
