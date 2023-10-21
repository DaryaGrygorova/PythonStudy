"""Representation of a binary tree data structure"""

class Node:
    """This represents both root node and a tree at the same time"""

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: int|float):
        assert type(data) in (int, float)

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print_self(self):
        # offset = 20
        # current_level = []
        # print(' ' * offset, end='')
        if self.left:
            self.left.print_self()
        print(self.data)
        if self.right:
            self.right.print_self()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_self()
