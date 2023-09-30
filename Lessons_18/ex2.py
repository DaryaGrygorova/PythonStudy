"""Iters"""


class MyIter:
    """Custom iter"""

    def __init__(self, init_storage=None):
        self.index = 0
        self.init_storage = init_storage or []

    def __iter__(
        self,
    ):  # this method call when call method iter() on instance of MyIter
        self.index = 0
        return self  # return self, because we need call custom method next from instance of MyIter

    def __next__(self):
        if self.index == len(self.init_storage):
            raise StopIteration
        self.index += 1
        return self.init_storage[self.index - 1]


my_iter = MyIter([1, 2, 3])  # instantiation - create object,
# initialization - add init attributes in instance

for item in my_iter:  # new_iterator_obj = iter(my_iter) == my.iter.__iter__()
    print(item)  # next(new_iterator_obj) == my_iter.__next__()

print("___________")
# for new_item in my_iter:
#     print(new_item)
# in details:
new_iterator_obj = iter(my_iter)  # iter(my_iter) is equal my_iter.__iter__()
while True:
    try:
        obj_inside_each_iteration = next(
            new_iterator_obj
        )  # next(new_iterator_obj) is equal new_iterator_obj.__next__,
           # and it is equal my_iter.__iter__().__next__()
        # action inside iteration (line 23)
        print(obj_inside_each_iteration)
    except StopIteration:
        # exit while-loop
        break
