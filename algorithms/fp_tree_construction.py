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
        self.node_link = None # Node links for connecting data with the same values. It will help us to explore the FP-Tree transversely

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
    

class HeaderTable:
    """
    Class for representing the header table of the FP-tree.

    This HeaderTable contain attributes and methods for tracking nodes with the same
    values in the FP-tree and linking them with node links.

    Arguments:
        item_support (dict): Dictionary with the counter of each item in the dataset.
    """
    def __init__(self, item_support: dict):
        self.table = {}
        for item, count in item_support.items():
            self.table[item] = {
                "node": None,
                "count": count
            }

    def add_node_link(self, node: Node):
        """
        Adds a node link between parent and child nodes.

        Arguments:
            node (Node class): Reference to the node from the Node class.
        """
        if node.value in self.table and self.table[node.value]["node"] is None:
            self.table[node.value]["node"] = node
        else:
            next_node = self.table[node.value]["node"]
            while next_node.node_link is not None:
                next_node = next_node.node_link
            next_node.node_link = node

    def get(self, value):
        """
        Gets the reference to the first appareance with item 'value'.

        Arguments:
            value (str): Value to search in the header table.

        Returns:
            Node class: Reference to the first node in the FP-tree with item
            `value`.
        """
        return self.table[value]
    
    def items(self):
        """Returns all items in the header table."""
        return self.table


def first_scan(data, header: list = None, minimum_support: int = 1):
    """
    Applies the first scan to obtain the support of the 1-item itemsets.

    Arguments:
        data (list): Dataset with items.
        header (list): List with the item's names.

    Returns:
        item_support (dict): Dictionary containing the support of the 1-item itemsets.
        item_order (list): List with the items sorted in descending order of support.
    """
    if header is None:
        raise ValueError("Header is missing.")

    # Getting item support
    item_support = {}
    for transaction in data:
        for i in range(len(transaction)):
            if header[i] in item_support:
                item_support[header[i]] += int(transaction[i])
            else:
                item_support[header[i]] = int(transaction[i])
    
    # Filter frequent items
    frequent_items = {item: count for item, count in item_support.items() if count >= minimum_support}

    # Sort by support. Descending order
    sorted_items = sorted(frequent_items.items(), key=lambda x: x[1], reverse=True)
    item_order = [item for item, _ in sorted_items]
    
    # Reconstruct filtered item_support dictionary in sorted order
    item_support = {item: frequent_items[item] for item in item_order}

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
    item_to_value = {item: value for item, value in zip(header, sample)}
    sorted_sample = [item_to_value[item] for item in item_order if item in item_to_value]

    return sorted_sample
    

def explore(sample, header, header_table: HeaderTable, tree: Node = None):
    """
    Searches the list for similarities with the values in the given tree.  
    If no similarities are found, a new node is created in the tree.

    Arguments:
        sample (list): A list containing the values to evaluate.
        header (list): A list of strings representing the names of the transaction items.
        header_table (HeaderTable): Header table for tracking nodes with same values.
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
                        explore(sample[i + 1:], header[i + 1:], header_table, tree=child)
                        found = True
                        break

                if not found:
                    child = Node(header[i], tree)
                    tree.add_child(child)
                    header_table.add_node_link(child)
                    explore(sample[i + 1:], header[i + 1:], header_table, tree=child)
                    break
                else:
                    break
                

def fp_tree_construction(dataset, minimum_support: int = 1, is_header: bool = True):
    """
    Builds the FP-tree from the input dataset.

    Args:
        dataset (list): A list of transactions, where each transaction is a list of items.
        is_header (bool): Boolean flag indicating whether the dataset includes a header in the first row.

    Returns:
        fp_tree (Node): The root of the FP-tree representing the itemsets in a tree structure.
        header_table (HeaderTable): The header table for tracking nodes with the same item.
    """
    # Split if header flag is True
    if is_header:
        header = dataset[0]
        data = dataset[1:]
    else:
        data = dataset
        
    # Check if the data set is in transaction or binary format and applies a transformaction in the first case
    target_list = ["1", "0", 1, 0, True, False]
    if isinstance(data, list) and all(isinstance(transaction, list) for transaction in data):
        if any(item in target_list for item in data[0]):
            pass
        else:
            data, header = transaction_to_binary(data)
    
    # First scan
    item_order, item_support = first_scan(data, header, minimum_support)

    # Second scan
    fp_tree = Node("root") # Tree initilization
    header_table = HeaderTable(item_support) # Header table initilization
    
    for sample in data:
        sorted_sample = sort_by_support(sample, header, item_order)
        explore(sorted_sample, item_order, header_table, fp_tree)

    return fp_tree, header_table