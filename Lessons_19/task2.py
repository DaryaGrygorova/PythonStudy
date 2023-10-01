"""Task 2
Create your own implementation of a built-in function range,
named in_range(), which takes three parameters: 'start', 'end',
and optional step.
Tips: See the documentation for 'range' function
"""


class MyRange:
    """Create custom range object"""

    def __init__(self, start, end, step):
        if step == 0:
            raise ValueError()
        self.index = 0
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        res = self.start + self.step * self.index
        if self.step > 0 and res >= self.end:
            raise StopIteration
        if self.step < 0 and self.end >= res:
            raise StopIteration
        self.index += 1
        return res

    def __str__(self):
        return (
            f"custom_range({self.start}, {self.end}"
            f'{f", {self.step}" if not self.step == 1 else ""})'
        )


def in_range(value, *args):
    """Custom range function"""
    start = 0
    end = value
    step = 1
    if len(args) == 1:
        start, end = value, args[0]
    if len(args) == 2:
        start, end, step = value, args[0], args[1]
    return MyRange(start, end, step)


print(in_range(5))  # custom_range(0, 5)
print(in_range(1, 5))  # custom_range(1, 5)
print(in_range(1, 6, 2))  # custom_range(1, 6, 2)

assert [*in_range(5)] == [*range(5)]
assert [*in_range(1, 5)] == [*range(1, 5)]
assert [*in_range(1, 6, 2)] == [*range(1, 6, 2)]
assert [*in_range(6, 1, -2)] == [*range(6, 1, -2)]
assert [*in_range(-6, 1, -2)] == [*range(-6, 1, -2)]
