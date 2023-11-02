"""
Task 1
Write a program that reads in a sequence of characters and prints
them in reverse order, using your implementation of Stack.
"""

from my_stack import MyStack


def print_revert_sequence(iterable):
    """Reads in a sequence of characters and prints them in reverse order"""
    new_stack = MyStack()
    for element in iterable:
        new_stack.push(element)
    for _ in range(new_stack.size()):
        print(new_stack.pop(), end=", ")
    # Delete extra characters from the end
    print("\b\b")


if __name__ == "__main__":
    print_revert_sequence("sequence")  # e, c, n, e, u, q, e, s
    print_revert_sequence(list(range(5)))  # 4, 3, 2, 1, 0
    print_revert_sequence(list(range(5, 0, -1)))  # 1, 2, 3, 4, 5
    print_revert_sequence(
        enumerate(range(5), 10)
    )  # (14, 4), (13, 3), (12, 2), (11, 1), (10, 0)
