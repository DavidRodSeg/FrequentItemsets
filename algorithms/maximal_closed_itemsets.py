"""
Methods for finding the maximal and closed itemsets within a tree structure.
"""


import copy


def find_closed(tree, minimum_support = 1, closed=None):
    """
    Finds the closed frequent itemsets in the specified tree.

    Arguments:
        tree (Node object): A tree-structured object containing frequent itemsets.
        minimum_support (int): The minimum support threshold to determine frequent itemsets.
        closed (list, optional): Accumulates closed frequent itemsets (default is None).

    Returns:
        list: A list of closed frequent itemsets.
    """
    same = False # Detects whether the node has the same countes as its child.
    if closed is None:
        closed = []

    for child in tree.children:
        if child.counter == tree.counter:
            same = True
        if child.counter >= minimum_support:
            find_closed(child, minimum_support, closed)

    if not same:
        item = tree.itemset()
        if item and item not in closed:
            closed.append(item)
    
    return closed


def find_maximal(tree, minimum_support = 1, maximal=None):
    """
    Finds the maximal frequent itemsets in the specified dataset.

    Arguments:
        tree (Node object): Tree structured object in which to find maximal
            frequent itemsets.
        minimum_support (int): The minimum support threshold to determine frequent itemsets.
        maximal (list, optional): Accumulates maximal frequent itemsets (default is None).

    Returns:
        list: A list of maximal frequent itemsets.
    """
    frequent = False # Detects whether the node has any frequent child.
    if maximal is None:
        maximal = []

    for child in tree.children:
        if child.counter >= minimum_support:
            find_maximal(child, minimum_support, maximal)
            frequent = True

    if not frequent:
        item = tree.itemset()
        if item and item not in maximal: # To avoid void values and repetitions.
            maximal.append(item)

    if maximal is None:
        raise ValueError("No maximal found.")
    else:
        return maximal


def find_closed_maximal(tree, minimum_support = 1, closed=None, maximal=None):
    """
    Finds the closed and maximal frequent itemsets in the specified tree.

    Arguments:
        tree (Node object): A tree-structured object containing frequent itemsets.
        minimum_support (int): The minimum support threshold to determine frequent itemsets.
        closed (list, optional): Accumulates closed frequent itemsets (default is None).
        maximal (list, optional): Accumulates maximal frequent itemsets (default is None).

    Returns:
        closed, maximal (tuple): A tuple containing two lists — the closed itemsets and the maximal itemsets.
    """
    same = False
    frequent = False
    if closed is None or maximal is None:
        closed = []
        maximal = []

    for child in tree.children:
        if child.counter == tree.counter:
            same = True
        if child.counter >= minimum_support:
            find_closed_maximal(child, minimum_support, closed, maximal)
            frequent = True

    if not frequent:
        item = tree.itemset()
        if item and item not in maximal:
            maximal.append(item)
            closed.append(item) # Maximal are closed, but not viceversa.
    elif not same:
        item = tree.itemset()
        if item and item not in closed:
            closed.append(item)
    
    return closed, maximal

  
def find_frequent(tree, minimum_support = 1):
    """
    Finds the frequent itemsets in the specified tree.

    Arguments:
        tree (Node object): A tree-structured object containing frequent itemsets.
        minimum_support (int): The minimum support threshold to determine frequent itemsets.

    Returns:
        list: A list containing the frequent itemsets.
    """
    maximal = find_maximal(tree, minimum_support)
    frequent = copy.deepcopy(maximal)

    for itemset in maximal:
        if len(itemset) > 1:
            temp_itemset = itemset[:]
            while len(temp_itemset) > 1:
                temp_itemset.pop()
                frequent.append(temp_itemset)
    
    return frequent