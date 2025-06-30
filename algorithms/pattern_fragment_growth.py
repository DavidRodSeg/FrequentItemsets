"""
Functions for mining frequent patterns with FP-tree by pattern fragment growth.
"""


from algorithms import Node, HeaderTable, fp_tree_construction
import time


def fp_growth(fp_tree: Node, header_table: HeaderTable, suffix: list = None, frequent_itemsets: list = None,
              minimum_support: int = 1):
    """
    Applies pattern fragment growth (FP-Growth) to mine the frequent itemsets for the 
    given FP-Tree.

    Arguments:
        fp_tree (Node): The FP-Tree that compactly represents the dataset.
        header_table (HeaderTable): The header table of the FP-Tree, containing references
            to the first occurrence of each item in the tree.
        suffix (list): List containing the suffix of the conditional path being explored.
        frequent_itemsets (list): List of the frequent itemsets.
        minimum_support (int): The minimum support threshold to determine frequent itemsets.
    """
    time.sleep(1)
    if suffix is None:
        suffix = []
    if frequent_itemsets is None:
        frequent_itemsets = []

    for item, key in sorted(header_table.table.items(), key=lambda x: x[1]["count"]):
        # Store the frequent itemsets
        new_suffix = suffix + [item]
        frequent_itemsets.append(new_suffix)

        # Find conditional pattern base
        conditional_pattern = []
        current_node = header_table.get(item)["node"]

        while current_node is not None:
            current_pattern = []
            parent = current_node.parent
            current_count = current_node.counter

            while parent is not None:
                current_pattern.append(parent.value)
                print(current_pattern)
                time.sleep(1)
                parent = parent.parent
            current_pattern.reverse()

            if current_pattern:
                for _ in range(current_count):
                    conditional_pattern.append(current_pattern)

            current_node = current_node.node_link

        # Build the new FP-Tree from the base
        conditional_tree, conditional_header_table = fp_tree_construction(conditional_pattern, minimum_support)

        # Apply fp_growth to the new tree recursively
        if conditional_header_table.table.items() and conditional_tree.children:
            frequent_itemsets = fp_growth(conditional_tree, conditional_header_table, new_suffix, frequent_itemsets, minimum_support)

    return frequent_itemsets