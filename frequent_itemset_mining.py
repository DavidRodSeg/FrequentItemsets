import csv
from algorithms import fp_growth_algorithm, find_closed_maximal, find_frequent


#################### LOADING THE DATA SET ####################
dataset = []
with open("prueba.csv", mode="r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    header = next(csv_reader)
    dataset.append(header)
    for row in csv_reader:
        dataset.append(row)

print(dataset)


#################### FP-GROWTH ALGORITHM ####################
itemsets = fp_growth_algorithm(dataset)


#################### CLOSED AND MAXIMAL ITEMSETS ####################
closed, maximal = find_closed_maximal(itemsets, minimum_support=1)
print(f"CLOSED ITEMSETS: {closed}")
print(f"MAXIMAL ITEMSETS: {maximal}")
frequent = find_frequent(itemsets, minimum_support=1)
print(f"FREQUENT ITEMSETS: {frequent}")