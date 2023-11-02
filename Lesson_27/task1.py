"""
Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево
та видалення піддерева з дерева, що існує.
"""


class Node:
    """Create a node with a references to left and right node"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_left(self, new_node):
        """Add reference to left node"""
        self.left = new_node

    def add_right(self, new_node):
        """Add reference to right node"""
        self.right = new_node


class BinaryTree:
    """Create a binary tree with a root object"""

    def __init__(self, root_data):
        self.node = Node(root_data)

    def get_right(self):
        """Returns right child of node"""
        return self.node.right

    def get_left(self):
        """Returns left child of node"""
        return self.node.left

    def get_value(self):
        """Returns value of node"""
        return self.node.data

    def add_left_node(self, data):
        """Add a new node as the left child of the current node"""
        if self.node.left is None:
            self.node.add_left(BinaryTree(data))
        else:
            raise ValueError("The left child of this node already exists")

    def add_right_node(self, data):
        """Add a new node as the right child of the current node"""
        if self.node.right is None:
            self.node.add_right(BinaryTree(data))
        else:
            raise ValueError("The right child of this node already exists")

    def add_left_subtree(self, tree):
        """Add a subtree to the left branch"""
        if not isinstance(tree, BinaryTree):
            raise ValueError("Type of tree must be BinaryTree")

        if self.node.left is None:
            self.node.add_left(tree)
        else:
            raise ValueError("The left child of this node already exists")

    def add_right_subtree(self, tree):
        """Add a subtree to the right branch"""
        if not isinstance(tree, BinaryTree):
            raise ValueError("Type of tree must be BinaryTree")

        if self.node.right is None:
            self.node.add_right(tree)
        else:
            raise ValueError("The right child of this node already exists")

    def remove_right_subtree(self):
        """Remove a subtree from the right branch of node"""
        if self.node.right is None:
            raise ValueError("This node hasn't right child")

        self.node.right = None

    def remove_left_subtree(self):
        """Remove a subtree from the left branch of node"""
        if self.node.left is None:
            raise ValueError("This node hasn't left child")

        self.node.left = None

    # def print_(self):
    #     """Print binary tree nodes with references"""
    #     current = self.node
    #     while current.left:
    #         print(
    #             "root",
    #             current.data,
    #             "[L]:",
    #             current.left.node.data if current.left else None,
    #             "[R]:",
    #             current.right.node.data if current.right else None,
    #         )
    #         if current.right:
    #             current.right.print_()
    #         current = current.left.node if current.left else None
    #
    #     current = self.node
    #     while current.right:
    #         print(
    #             "root",
    #             current.data,
    #             "[L]:",
    #             current.left.node.data if current.left else None,
    #             "[R]:",
    #             current.right.node.data if current.right else None,
    #         )
    #         if current.left:
    #             current.left.print_()
    #         current = current.right.node if current.right else None


new_tree = BinaryTree("0")
new_tree.add_left_node("1")
new_tree.add_right_node("2")
left_child = new_tree.get_left()
right_child = new_tree.get_right()
left_child.add_left_node("3")
left_child.add_right_node("4")
right_child.add_left_node("5")
right_child.add_right_node("6")
assert left_child.get_value() == "1"
assert right_child.get_value() == "2"
assert left_child.get_left().get_value() == "3"
assert left_child.get_right().get_value() == "4"
assert right_child.get_left().get_value() == "5"
assert right_child.get_right().get_value() == "6"

another_tree = BinaryTree("7")
another_tree.add_left_node("8")
another_tree.add_right_node("9")
another_left_child = another_tree.get_left()
another_right_child = another_tree.get_right()
another_left_child.add_left_node("10")
another_left_child.add_right_node("11")
another_right_child.add_left_node("12")
another_right_child.add_right_node("13")

assert another_left_child.get_value() == "8"
assert another_right_child.get_value() == "9"
assert another_left_child.get_left().get_value() == "10"
assert another_left_child.get_right().get_value() == "11"
assert another_right_child.get_left().get_value() == "12"
assert another_right_child.get_right().get_value() == "13"

new_tree.get_left().get_left().add_left_subtree(another_tree)
assert left_child.get_left().get_right() is None
assert left_child.get_left().get_left().get_value() is another_tree.get_value()

assert another_right_child.get_left().get_value() == "12"
another_tree.get_right().remove_left_subtree()
assert another_right_child.get_left() is None
assert left_child.get_left().get_left().get_right().get_left() is None
