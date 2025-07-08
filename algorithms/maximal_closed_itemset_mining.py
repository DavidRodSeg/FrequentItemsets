"""
Methods for finding the maximal and closed itemsets within a tree structure.
"""


def sort_frequent_itemsets(freq_itemsets: dict):
    """
    Sorts the frequent itemsets dictionary lexicographically.

    Arguments:
        freq_itemsets (dict): A dictionary containing frequent itemsets and their respective support.

    Returns:
        sorted_freq_itemsets (dict): The sorted frequent itemsets dictionary.
    """
    sorted_items_dict = {tuple(sorted(key)) : value for (key, value) in freq_itemsets.items()}
    sorted_frequent_itemsets = {key : sorted_items_dict[key] for key in sorted(sorted_items_dict)}

    return sorted_frequent_itemsets


def find_closed_itemsets(freq_itemsets: dict, order: bool = True):
    """
    Finds the closed frequent itemsets in the specified tree.

    Arguments:
        freq_itemsets (dict): A dictionary containing frequent itemsets and their respective support.
        order (bool): Flag indicating whether to order the itemsets.

    Returns:
        closed_itemsets (list): A list of closed frequent itemsets.
    """
    if order:
        sorted_frequent_itemsets = sort_frequent_itemsets(freq_itemsets)

    closed_itemsets = {}
    for (itemset, support) in sorted_frequent_itemsets.items():
        is_closed = True
        for (itemset2, support2) in sorted_frequent_itemsets.items():
            if set(itemset) < set(itemset2) and support == support2: # The comparison must be made with sets, as lists have order
                is_closed = False
                break

        if is_closed:
            closed_itemsets[itemset] = support

    return closed_itemsets


def find_maximal_itemsets(freq_itemsets: dict, order: bool = True):
    """
    Finds the maximal frequent itemsets in the specified dataset.

    Arguments:
        freq_itemsets (dict): A dictionary containing frequent itemsets and their respective support.
        order (bool): Flag indicating whether to order the itemsets.

    Returns:
        list: A list of maximal frequent itemsets.
    """
    if order:
        sorted_frequent_itemsets = sort_frequent_itemsets(freq_itemsets)

    maximal_itemsets = {}
    for (itemset, support) in sorted_frequent_itemsets.items():
        is_maximal = True
        for (itemset2, _) in sorted_frequent_itemsets.items():
            if set(itemset) < set(itemset2):
                is_maximal = False
                break

        if is_maximal:
            maximal_itemsets[itemset] = support

    return maximal_itemsets


def find_closed_maximal(freq_itemsets: dict, order: bool = True):
    """
    Finds the closed and maximal frequent itemsets in the specified tree.

    Arguments:
        freq_itemsets (dict): A dictionary containing frequent itemsets and their respective support.
        order (bool): Flag indicating whether to order the itemsets.

    Returns:
        closed, maximal (tuple): A tuple containing two lists — the closed itemsets and the maximal itemsets.
    """
    closed_itemsets = find_closed_itemsets(freq_itemsets, order)
    maximal_itemsets = find_maximal_itemsets(freq_itemsets, order)

    return closed_itemsets, maximal_itemsets