"""
Main script for frequent itemsets mining.

To execute it use `python frequent_itemset_mining.py file_path min_support`.
"""
import csv
import sys
from algorithms import fp_tree_construction, find_closed_maximal, fp_growth, sort_frequent_itemsets


# Error pruning
if len(sys.argv) != 3: # The name of the file is taken as an argument
    raise ValueError("Not enough parameters provided!")

file_path = sys.argv[1]
min_support = int(sys.argv[2]) # Sys arguments are strings by default


#################### LOADING THE DATA SET ####################
dataset = []
with open(file_path, mode="r") as file:
    # Get the delimiter used in the dataset using the Sniffer class of the CSV internal library
    sample = file.read(1024)
    dialect = csv.Sniffer().sniff(sample)
    delimiter = dialect.delimiter

    # Reset CSV pointer
    file.seek(0)

    # Read the dataset
    csv_reader = csv.reader(file, delimiter=delimiter)
    header = next(csv_reader)
    dataset.append(header)
    for row in csv_reader:
        dataset.append(row)


#################### FP-GROWTH ALGORITHM ####################
_, header_table = fp_tree_construction(dataset, min_support)
frequent_itemsets = fp_growth(header_table, minimum_support=min_support)
frequent_itemsets = sort_frequent_itemsets(frequent_itemsets)
print(f"FREQUENT ITEMSETS: {frequent_itemsets}")


#################### CLOSED AND MAXIMAL ITEMSETS ####################
closed, maximal = find_closed_maximal(frequent_itemsets)
print(f"CLOSED ITEMSETS: {closed}")
print(f"MAXIMAL ITEMSETS: {maximal}")