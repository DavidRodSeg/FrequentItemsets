"""
Functions for applying the FP-Growth algorithm.
"""

from tree_class.tree import Node
from utils.conversions import transaction2binary


def explore(sample, header, tree=None):
    """
    Explore the list to search for similarities with the values in the tree class passed as argument. 
    If no similarities are found, a new node is created in the tree.

    Args:
        list (pd.DataFrame): A Pandas DataFrame containing the values to evaluate.
        tree (Node class): The root node in the tree structure to compare with (default: None).
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
                

def fp_growth_algorithm(dataset):
    """
    Applies the FP-Growth algorithm to the input data set.

    Args:
        dataset (list): Data set with items.
    
    Returns:
        freq_itemsets (Node class): List containing the frequen itemsets.
    """
    # Check if the data set is in transaction or binary format and applies a transformaction in the first case
    target_list = ["1", "0", 1, 0, True, False]
    if isinstance(dataset, list) and all(isinstance(transaction, list) for transaction in dataset):
        if any(item in target_list for item in set(dataset[1])):
            pass
        else:
            dataset = transaction2binary(dataset)
    header = dataset[0]
    data = dataset[1:]
    freq_itemsets = Node("root") # Tree initilization
    
    for sample in data:
        explore(sample, header, freq_itemsets)

    return freq_itemsets