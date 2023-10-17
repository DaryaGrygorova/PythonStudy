"""
My implementation of Stack.
"""


class MyStack:
    """
    Create linear data structure that stores items
    in a Last-In/First-Out (LIFO)
    or First-In/Last-Out (FILO) manner
    """
    def __init__(self):
        self._items = []

    def empty(self):
        """Returns True or False depending on whether the stack is empty"""
        return not self._items

    def peek(self):
        """Returns a reference to the topmost element of the stack or None if stack is empty"""
        return self._items[len(self._items) - 1] if not self.empty() else None

    def push(self, item):
        """Inserts the element at the top of the stack"""
        self._items.append(item)

    def pop(self):
        """Deletes and returns the topmost element of the stack or None if stack is empty"""
        return self._items.pop() if not self.empty() else None

    def size(self):
        """Returns the size of the stack"""
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation
