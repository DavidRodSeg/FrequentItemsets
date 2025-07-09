"""
Functions for mining frequent patterns with FP-tree by pattern fragment growth.
"""


from algorithms import HeaderTable, fp_tree_construction


def _fp_growth_recursive(header_table: HeaderTable, suffix: list = None, frequent_itemsets: dict = None,
              minimum_support: int = 1):
    """
    Private recursive implementation of the FP-Growth algorithm.

    Applies pattern fragment growth (FP-Growth) to mine the frequent itemsets for the 
    given FP-Tree.

    Arguments:
        header_table (HeaderTable): The header table of the FP-Tree, containing references
            to the first occurrence of each item in the tree.
        suffix (list): List containing the suffix of the conditional path being explored.
        frequent_itemsets (dict): Dictionary of the frequent itemsets.
        minimum_support (int): The minimum support threshold to determine frequent itemsets.

    Returns:
        frequent_itemsets (dict): Dictionary of the frequent itemsets.
    """
    if suffix is None:
        suffix = []
    if frequent_itemsets is None:
        frequent_itemsets = {}

    for item, links_counts in reversed(header_table.table.items()):
        # Store the frequent itemsets
        new_suffix = suffix + [item]
        frequent_itemsets[tuple(new_suffix)] = links_counts["count"]

        # Find conditional pattern base
        conditional_pattern = []
        current_node = header_table.get(item)["node"]

        while current_node is not None:
            current_pattern = []
            parent = current_node.parent
            current_count = current_node.counter

            while parent.value != "root":
                current_pattern.append(parent.value)
                parent = parent.parent
            current_pattern.reverse()

            if current_pattern:
                for _ in range(current_count):
                    conditional_pattern.append(current_pattern)

            current_node = current_node.node_link

        # Build the new FP-Tree from the base and apply fp_growth to the new tree recursively
        if conditional_pattern:
            conditional_tree, conditional_header_table = fp_tree_construction(conditional_pattern, minimum_support, is_header=False)

            if conditional_header_table.table.items() and conditional_tree.children:
                frequent_itemsets = _fp_growth_recursive(conditional_header_table, new_suffix, frequent_itemsets, minimum_support)

    return frequent_itemsets


def fp_growth(header_table: HeaderTable, minimum_support: int = 1):
    """
    Applies pattern fragment growth (FP-Growth) to mine the frequent itemsets for the 
    given FP-Tree.

    Arguments:
        header_table (HeaderTable): The header table of the FP-Tree, containing references
            to the first occurrence of each item in the tree.
        minimum_support (int): The minimum support threshold to determine frequent itemsets.

    Returns:
        frequent_itemsets (dict): Dictionary of the frequent itemsets.
    """
    return _fp_growth_recursive(header_table, minimum_support=minimum_support)