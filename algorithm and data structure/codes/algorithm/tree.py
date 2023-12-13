class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def is_leaf(self):
        return len(self.children) == 0

class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_node(self, parent_value, child_value):
        parent_node = self.find_node(self.root, parent_value)
        if parent_node is not None:
            parent_node.add_child(Node(child_value))

    def find_node(self, current_node, value):
        if current_node.value == value:
            return current_node
        for child in current_node.children:
            node = self.find_node(child, value)
            if node is not None:
                return node
        return None

    def print_tree(self, node, level=0, prefix="Root: "):
        indent = " " * (level * 4)
        print(indent + prefix + str(node.value))
        for child in node.children:
            child_prefix = "└── " if child == node.children[-1] else "├── "
            self.print_tree(child, level + 1, child_prefix)

    def get_depth(self, node):
        depth = 0
        while node.parent:
            node = node.parent
            depth += 1
        return depth

    def find_siblings(self, value):
        node = self.find_node(self.root, value)
        if node and node.parent:
            return [child.value for child in node.parent.children if child != node]
        return []

# Example Usage
my_tree = Tree("Root")
my_tree.add_node("Root", "Child1")
my_tree.add_node("Root", "Child2")
my_tree.add_node("Child1", "Grandchild1")
my_tree.add_node("Child1", "Grandchild2")
my_tree.add_node("Child2", "Grandchild3")

print("Tree Structure:")
my_tree.print_tree(my_tree.root)

print("\nDepth of 'Grandchild1':", my_tree.get_depth(my_tree.find_node(my_tree.root, "Grandchild1")))

print("\nSiblings of 'Grandchild1':", my_tree.find_siblings("Grandchild1"))
