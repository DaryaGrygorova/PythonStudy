"""
Task 2
Implement a stack using a singly linked list.
"""

from Lesson_25.node import Node


class MyLinkedStack:
    """
    Create linear data structure that stores items
    in a Last-In/First-Out (LIFO)
    or First-In/Last-Out (FILO) manner
    using a singly linked list
    """

    def __init__(self):
        self._head = None

    def empty(self):
        """Returns True or False depending on whether the stack is empty"""
        return self._head is None

    def peek(self):
        """Returns a reference to the topmost element of the stack or None if stack is empty"""
        if self.empty():
            return None

        current = self._head

        # Search last element in the list
        while current.get_next() is not None:
            current = current.get_next()

        return current.get_data()

    def push(self, item):
        """Pushes the element at the top of the stack"""
        new_node = Node(item)

        if self.empty():
            self._head = new_node
            return None

        current = self._head

        # Search last element in the list
        while current.get_next() is not None:
            current = current.get_next()

        # Rewrite a reference
        current.set_next(new_node)

        return None

    def pop(self):
        """Deletes and returns the topmost element of the stack or None if stack is empty"""
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
        """Returns the size of the stack"""
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def __repr__(self):
        representation = "<Stack: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    new_stack = MyLinkedStack()
    for num in range(1, 11):
        new_stack.push(f"{num}")

    print(new_stack)  # <Stack: 1 2 3 4 5 6 7 8 9 10 >

    assert new_stack.peek() == "10"  # <Stack: 1 2 3 4 5 6 7 8 9 10 >
    assert new_stack.size() == 10  # <Stack: 1 2 3 4 5 6 7 8 9 >
    assert new_stack.pop() == "10"  # <Stack: 1 2 3 4 5 6 7 8 9 >
    assert new_stack.size() == 9  # <Stack: 1 2 3 4 5 6 7 8 9 >

    assert new_stack.peek() == "9"  # <Stack: 1 2 3 4 5 6 7 8 9 >
    assert new_stack.pop() == "9"  # <Stack: 1 2 3 4 5 6 7 8  >
    assert new_stack.peek() == "8"  # <Stack: 1 2 3 4 5 6 7 8 >
    assert new_stack.pop() == "8"  # <Stack: 1 2 3 4 5 6 7 >
    assert new_stack.peek() == "7"  # <Stack: 1 2 3 4 5 6 7 >
    print(new_stack)  # <Stack: 1 2 3 4 5 6 7 >

    new_stack.push("9")  # <Stack: 1 2 3 4 6 7 9 >
    new_stack.push("8")  # <Stack: 1 2 3 4 5 6 7 9 8 >
    new_stack.push("new_item")  # <Stack: 1 2 3 4 5 6 7 9 8 new_item >
    print(new_stack)  # <Stack: 1 2 3 4 5 6 7 9 8 new_item >
