"""
Classes and functions for constructing the FP-tree.
"""


from utils.conversions import transaction_to_binary


class Node:
    """
    Tree node class for the creation of a tree structure.

    Arguments:
        value (str): Value associated with the node.
        parent (object): Reference to the parent node (default is None).
    """
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.counter = 1
        self.parent = parent

    def add_child(self, child):
        """
        Adds child node to the children list.

        Arguments:
            child (Node class): Child node.
        """
        self.children.append(child)
    
    def count(self):
        """
        Increases the internal counter of the itemset.
        """
        self.counter += 1

    def itemset(self):
        """
        Returns the transaction representation of the current itemset.
        """
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

        Arguments:
            key (str): Value of the child to consider.
        """
        if key == self.value:
            return self.to_dict()
        for child in self.children:
            try:
                return child[key] # It's the same as "child.__getitem__(key)"
            except KeyError:
                continue
        raise KeyError(f"No node found with value: {key}")


def first_scan(dataset, minimum_support):
    """
    Applies the first scan to obtain the support of the 1-item itemsets.

    Arguments:
        dataset (list): Data set with items.

    Returns:
        item_support (dict): Dictionary containing the support of the 1-item itemsets.
        item_order (list): List with the items sorted in descending order of support.
    """
    target_list = ["1", "0", 1, 0, True, False]
    if isinstance(dataset, list) and all(isinstance(transaction, list) for transaction in dataset):
        if any(item in target_list for item in set(dataset[1])): # REVISAR: Is set necessary?
            pass
        else:
            dataset = transaction_to_binary(dataset)

    header = dataset[0]
    data = dataset[1:]

    item_support = {}
    for transaction in data:
        for i in range(len(transaction)):
            if header[i] in item_support:
                item_support[header[i]] += int(transaction[i])
            else:
                item_support[header[i]] = 1

    item_order = list(dict(sorted(item_support.items(), key=lambda item: item[1] if item[1] >= minimum_support else None, reverse=True)))

    # Delete not frequent items
    for key in list(item_support):
        if key not in item_order:
            item_support.pop(key, None)

    return item_order, item_support


def sort_by_support(sample, header, item_order):
    """
    Sort the items in the sample by the specified order.

    Arguments:
        sample (list): A list containing the values to evaluate.
        header (list): A list of strings representing the names of the transaction items.
        item_order (list): List with the items sorted in descending order of support.

    Returns:
        sorted_sample (list): The list containing the values to evaluate, but sorted.
    """
    sorted_idx = [idx for value in header for idx, value_ord in enumerate(item_order) if value_ord == value] # If value is not in item_order, then it will be omitted which is what we expect
    sorted_sample = [sample[idx] for idx in sorted_idx]

    return sorted_sample  
    

def explore(sample, header, tree=None):
    """
    Searches the list for similarities with the values in the given tree.  
    If no similarities are found, a new node is created in the tree.

    Arguments:
        sample (list): A list containing the values to evaluate.
        header (list): A list of strings representing the names of the transaction items.
        tree (Node): The root node of the tree structure to expand (default: None).
    """

    if tree is None:
        raise(ValueError("No tree has been passed."))
    else:
        for i in range(len(sample)):
            if int(sample[i]) == 1:
                found = False
                for child in tree.children:
                    if header[i] == child.value:         
                        child.count()
                        explore(sample[i + 1:], header[i + 1:], tree=child)
                        found = True
                        break

                if not found:
                    child = Node(header[i], tree)
                    tree.add_child(child)
                    explore(sample[i + 1:], header[i + 1:], tree=child)
                    break
                else:
                    break
                

def fp_tree_construction(dataset, minimum_support: int = 1):
    """
    Builds the FP-tree to the input data set.

    Arguments:
        dataset (list): Data set with items.
    
    Returns:
        freq_itemsets (Node class): Object that contains the itemsets
            in a tree-structure.
    """
    # Check if the data set is in transaction or binary format and applies a transformaction in the first case
    target_list = ["1", "0", 1, 0, True, False]
    if isinstance(dataset, list) and all(isinstance(transaction, list) for transaction in dataset):
        if any(item in target_list for item in set(dataset[1])):
            pass
        else:
            dataset = transaction_to_binary(dataset)
    
    # First scan
    item_order, _ = first_scan(dataset, minimum_support)

    # Second scan
    header = dataset[0]
    data = dataset[1:]

    freq_itemsets = Node("root") # Tree initilization
    
    for sample in data:
        sorted_sample = sort_by_support(sample, header, item_order)
        explore(sorted_sample, header, freq_itemsets)

    return freq_itemsets