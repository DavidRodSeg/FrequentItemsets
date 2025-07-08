import csv
from algorithms import fp_tree_construction, find_closed_maximal, fp_growth


#################### LOADING THE DATA SET ####################
dataset = []
with open("prueba.csv", mode="r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    header = next(csv_reader)
    dataset.append(header)
    for row in csv_reader:
        dataset.append(row)


#################### FP-GROWTH ALGORITHM ####################
_, header_table = fp_tree_construction(dataset)
frequent_itemsets = fp_growth(header_table)
print(f"FREQUENT ITEMSETS: {frequent_itemsets}")


#################### CLOSED AND MAXIMAL ITEMSETS ####################
closed, maximal = find_closed_maximal(frequent_itemsets)
print(f"CLOSED ITEMSETS: {closed}")
print(f"MAXIMAL ITEMSETS: {maximal}")