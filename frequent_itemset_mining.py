import csv
from algorithms.fp_growth import fp_growth_algorithm
from algorithms.maximal_closed_itemsets import find_closed_maximal, find_frequent


#################### LOADING THE DATA SET ####################
dataset = []
with open("market.csv", mode="r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    header = next(csv_reader)
    dataset.append(header)
    for row in csv_reader:
        dataset.append(row)


#################### FP-GROWTH ALGORITHM ####################
itemsets = fp_growth_algorithm(dataset)


#################### CLOSED AND MAXIMAL ITEMSETS ####################
closed, maximal = find_closed_maximal(itemsets, minimum_support=40)
print(f"CLOSED ITEMSETS: {closed}")
print(f"MAXIMAL ITEMSETS: {maximal}")