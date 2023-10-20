"""
Task 3
Implement a queue using a singly linked list.
"""

from Lesson_25.node import Node


class MyLinkedQueue:
    """Create linear data structure that stores items
    in a First-in-First-Out (FIFO) manner
    using a singly linked list
    """

    def __init__(self):
        self._head = None

    def empty(self):
        """Returns True or False depending on whether the stack is empty"""
        return self._head is None

    def enqueue(self, item):
        """Adds an element to the end of the queue"""
        new_node = Node(item)
        new_node.set_next(self._head)
        self._head = new_node

    def dequeue(self):
        """Removes the element at the beginning of the queue or None if queue is empty"""
        if self.empty():
            return None

        current = self._head
        prev = None

        # Search last element in the list
        while current.get_next() is not None:
            prev = current
            current = current.get_next()

        # Rewrite a reference
        prev.set_next(None)

        return current.get_data()

    def size(self):
        """Returns the size of the queue"""
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def __repr__(self):
        representation = "<Queue: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    new_queue = MyLinkedQueue()
    for num in range(1, 11):
        new_queue.enqueue(f"{num}")

    print(new_queue)  # <Queue: 10 9 8 7 6 5 4 3 2 1 >

    assert new_queue.size() == 10  # <Queue: 10 9 8 7 6 5 4 3 2 1 >
    assert new_queue.dequeue() == "1"  # <Queue: 10 9 8 7 6 5 4 3 2 >
    assert new_queue.size() == 9  # <Queue: 10 9 8 7 6 5 4 3 2 >

    assert new_queue.dequeue() == "2"  # <Queue: 10 9 8 7 6 5 4 3 >

    print(new_queue)  # <Queue: 10 9 8 7 6 5 4 3 >

    new_queue.enqueue("1")  # <Queue: 1 10 9 8 7 6 5 4 3 >
    new_queue.enqueue("2")  # <Queue: 2 1 10 9 8 7 6 5 4 3 >
    new_queue.enqueue("new_item")  # <Queue: new_item 2 1 10 9 8 7 6 5 4 3 >
    print(new_queue)  # <Queue: new_item 2 1 10 9 8 7 6 5 4 3 >
