import csv
from algorithms import fp_tree_construction, find_closed_maximal, find_frequent, fp_growth


#################### LOADING THE DATA SET ####################
dataset = []
with open("prueba.csv", mode="r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    header = next(csv_reader)
    dataset.append(header)
    for row in csv_reader:
        dataset.append(row)

# print(dataset)


#################### FP-GROWTH ALGORITHM ####################
fp_tree, header_table = fp_tree_construction(dataset)
frequent_itemsets = fp_growth(fp_tree, header_table)
print(f"FREQUENT ITEMSETS: {frequent_itemsets}")


#################### CLOSED AND MAXIMAL ITEMSETS ####################
closed, maximal = find_closed_maximal(frequent_itemsets, minimum_support=1)
print(f"CLOSED ITEMSETS: {closed}")
print(f"MAXIMAL ITEMSETS: {maximal}")
frequent = find_frequent(frequent_itemsets, minimum_support=1)
print(f"FREQUENT ITEMSETS: {frequent}")