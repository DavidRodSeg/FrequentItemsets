"""
Classes for creating a tree structure.
"""

class Node:
    """
    Tree node class for the creation of a tree structure.

    Args:
        value (str): Value associated with the node.
    """
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.counter = 1
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)
    
    def count(self):
        self.counter += 1

    def itemset(self):
        if self.parent is None and self.value != "root":
            raise ValueError("No parent itemset provided.")
        elif self.value == "root":
            return []
        else:
            return self.parent.itemset() + [self.value]
    
    def to_dict(self):
        """
        Converts the tree rooted at this node into a dictionary representation.
        """
        tree = {
            self.value: self.counter,
            "children": []
            }
        for child in self.children:
            tree["children"].append(child.to_dict())
        return tree

    def __getitem__(self, key):
        """
        Allows dictionary-like access to child nodes by their value.
        """
        if key == self.value:
            return self.to_dict()
        for child in self.children:
            try:
                return child[key] # It's the same as "child.__getitem__(key)"
            except KeyError:
                continue
        raise KeyError(f"No node found with value: {key}")