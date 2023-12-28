class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def display(self):
        self._display_recursive(self.root)

    def _display_recursive(self, node):
        if node is not None:
            self._display_recursive(node.left)
            print(node.value)
            self._display_recursive(node.right)

# Example Usage
tree = BinaryTree()
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.display()
