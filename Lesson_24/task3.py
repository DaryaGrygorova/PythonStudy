"""
Task 3
Extend the Stack to include a method called get_from_stack that
searches and returns an element e from a stack. Any other element
must remain on the stack respecting their order.
Consider the case in which the element is not found -
raise ValueError with proper info Message

Extend the Queue to include a method called get_from_stack that
searches and returns an element e from a queue. Any other element
must remain in the queue respecting their order.
Consider the case in which the element is not found -
raise ValueError with proper info Message
"""

from my_stack import MyStack
from my_queue import MyQueue


class MyExtendedStack(MyStack):
    """Extend the MyStack to include a method called get_from_stack"""

    def __init__(self):
        super().__init__()
        self.temp = MyStack()
        self.temp_item = None

    def get_from_stack(self, element):
        """Searches, removes and returns an element from a stack"""
        for _ in range(self.size()):
            self.temp_item = self.pop()
            if element == self.temp_item:
                break
            self.temp.push(self.temp_item)

        for _ in range(self.temp.size()):
            self.push(self.temp.pop())

        if not self.temp_item:
            raise ValueError("Element not found in stack!")

        result = self.temp_item
        self.temp_item = None
        return result


class MyExtendedQueue(MyQueue):
    """Extend the MyQueue to include a method called get_from_queue"""

    def __init__(self):
        super().__init__()
        self.temp = MyQueue()
        self.temp_item = None

    def get_from_queue(self, element):
        """Searches, removes and returns an element from a stack"""
        for _ in range(self.size()):
            self.temp_item = self.dequeue()
            if element == self.temp_item:
                continue
            self.temp.enqueue(self.temp_item)

        for _ in range(self.temp.size()):
            self.enqueue(self.temp.dequeue())

        if not self.temp_item:
            raise ValueError("Element not found in queue!")

        result = self.temp_item
        self.temp_item = None
        return result


if __name__ == "__main__":
    new_stack = MyExtendedStack()
    for num in range(1, 6):
        new_stack.push(f"{num}")
    print(new_stack)  # <Stack>: 1: 5, 2: 4, 3: 3, 4: 2, 5: 1

    new_stack.get_from_stack("3")
    print(new_stack)  # <Stack>: 1: 5, 2: 4, 3: 2, 4: 1

    new_stack.get_from_stack("5")
    print(new_stack)  # <Stack>: 1: 4, 2: 2, 3: 1

    new_queue = MyExtendedQueue()
    for num in range(1, 6):
        new_queue.enqueue(f"{num}")
    print(new_queue)  # <Queue>: 1: 1, 2: 2, 3: 3, 4: 4, 5: 5

    new_queue.get_from_queue("4")
    print(new_queue)  # <Queue>: 1: 1, 2: 2, 3: 3, 4: 5

    new_queue.get_from_queue("1")
    print(new_queue)  # <Queue>: 1: 2, 2: 3, 3: 5
