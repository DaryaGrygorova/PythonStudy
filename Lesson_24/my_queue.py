"""
My implementation of Queue.
"""


class MyQueue:
    """Create linear data structure that stores items
    in a First-in-First-Out (FIFO) manner"""

    def __init__(self):
        self._items = []

    def empty(self):
        """Returns True or False depending on whether the stack is empty"""
        return not self._items

    def enqueue(self, item):
        """Adds an element to the end of the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Removes the element at the beginning of the queue or None if queue is empty"""
        if self.size() < 1:
            return None
        return self._items.pop() if not self.empty() else None

    def size(self):
        """Returns the size of the queue"""
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation
