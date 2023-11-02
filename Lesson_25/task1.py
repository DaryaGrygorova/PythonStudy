"""
Task 1 - Extend UnorderedList
Implement append, index, pop, insert methods for UnorderedList.
Also implement a slice method, which will take two parameters 'start' and
'stop', and return a copy of the list starting at the position and going up
to but not including the stop position.
"""

from node import Node


class MyExtendedUnorderedList:
    """
    A set of elements, each containing a value and
    a reference to the next element in the list.
    The class also contains a reference to the first
    element of the list. For simplicity, we will assume
    that lists cannot contain duplicate elements.
    """

    def __init__(self):
        self._head = None

    def empty(self):
        """Return True if list is empty"""
        return self._head is None

    def add(self, item):
        """Adds new element to start of the list"""
        new_node = Node(item)
        new_node.set_next(self._head)
        self._head = new_node

    def append(self, item):
        """Adds new element to end of the list"""
        new_node = Node(item)

        if self.empty():
            self._head = new_node
            return

        current = self._head

        # Search last element in the list
        while current.get_next() is not None:
            current = current.get_next()

        # Rewrite a reference
        current.set_next(new_node)

    def index(self, item):
        """Returns index of item"""
        current = self._head
        index = 0

        # Search item in the list
        while current is not None:
            if current.get_data() == item:
                return index
            current = current.get_next()
            index += 1
        raise ValueError("Element not found in the list!")

    def pop(self, index=None):
        """Remove item at given index"""
        if self.empty():
            raise IndexError("Pop from empty list!")

        index = (self.size() - 1) if index is None else index

        if self.size() <= index:
            raise IndexError("Pop index out of range!")

        if index == 0:
            value = self._head.get_data()
            self._head = self._head.get_next()

            return value

        current = self._head
        prev = self._head
        count = 1

        # Search element with given index
        while current is not None and count != (index + 1):
            count += 1
            prev = current
            current = current.get_next()

        # Rewrite a reference to the next element
        value = current.get_data()
        prev.set_next(current.get_next())
        return value

    def insert(self, index, item):
        """Inserts item at given position"""
        if self.empty() or index == 0:
            self.add(item)
            return

        if self.size() < index:
            raise IndexError("Pop index out of range!")

        new_node = Node(item)
        current = self._head
        prev = self._head
        count = 1

        # Search element with given index
        while current is not None and count != (index + 1):
            count += 1
            prev = current
            current = current.get_next()

        # Rewrite a reference
        prev.set_next(new_node)
        new_node.set_next(current)

    def slice(self, start, stop):
        """Returns a copy of the list starting at the position
        and going up to but not including the stop position"""
        sliced_list = MyExtendedUnorderedList()

        if self.empty():
            raise IndexError("List is empty!")

        if self.size() <= start:
            raise IndexError("Start index out of range!")

        if stop <= start:
            raise IndexError("The stop index must be greater than the start index!")

        current = self._head
        index = 1

        while current is not None and index <= start:
            index += 1
            current = current.get_next()

        while current is not None and index <= stop:
            index += 1
            sliced_list.append(current.get_data())
            current = current.get_next()

        return sliced_list

    def size(self):
        """Returns count of elements in the list"""
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    new_list = MyExtendedUnorderedList()
    for num in range(2, 11):
        new_list.append(f"{num}")

    print(new_list)  # <UnorderedList: 2 3 4 5 6 7 8 9 10 >
    new_list.add("1")

    print(new_list)  # <UnorderedList: 1 2 3 4 5 6 7 8 9 10 >
    assert new_list.index("1") == 0
    assert new_list.index("5") == 4
    assert new_list.index("10") == 9

    assert new_list.pop() == "10"  # <UnorderedList: 1 2 3 4 5 6 7 8 9 >
    assert new_list.pop(0) == "1"  # <UnorderedList: 2 3 4 5 6 7 8 9 >
    assert new_list.pop(7) == "9"  # <UnorderedList: 2 3 4 5 6 7 8 >
    assert new_list.pop(3) == "5"  # <UnorderedList: 2 3 4 6 7 8 >
    print(new_list)  # <UnorderedList: 2 3 4 6 7 8 >

    new_list.insert(0, "1")  # <UnorderedList: 1 2 3 4 6 7 8 >
    new_list.insert(4, "5")  # <UnorderedList: 1 2 3 4 5 6 7 8 >
    new_list.insert(8, "9")  # <UnorderedList: 1 2 3 4 5 6 7 8 9 >
    new_list.insert(9, "10")  # <UnorderedList: 1 2 3 4 5 6 7 8 9 10>
    print(new_list)  # <UnorderedList: 1 2 3 4 5 6 7 8 9 10 >

    assert new_list.slice(0, 3).size() == 3  # <UnorderedList: 1 2 3 >
    assert new_list.slice(2, 3).size() == 1  # <UnorderedList: 3 >
    assert new_list.slice(3, 7).size() == 4  # <UnorderedList: 4 5 6 7 >
    assert new_list.slice(5, 11).size() == 5  # <UnorderedList: 6 7 8 9 10 >
    print(new_list)  # <UnorderedList: 1 2 3 4 5 6 7 8 9 10 >
