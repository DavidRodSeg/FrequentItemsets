"""
Tests for checking maximal_closed_itemsets module functions.
"""


from algorithms import fp_growth_algorithm, find_maximal, find_closed, find_closed_maximal, find_frequent


#################### SIMPLE CASE ####################
print("SIMPLE CASE \n")
dataset = [["apple", "banana", "orange", "tomato"],
           [1, 0, 0, 1],
           [0, 1, 1, 1],
           [1, 1, 0, 1],
           [0, 0, 0, 1]]

itemsets = fp_growth_algorithm(dataset)
print(f"- FREQUENT ITEMSETS: {itemsets.to_dict()} \n")

closed = find_closed(itemsets, minimum_support=2)
print(f"- CLOSED ITEMSETS: {closed} \n")

maximal = find_maximal(itemsets, minimum_support=2)
print(f"- MAXIMAL ITEMSETS: {maximal} \n")

closed, maximal = find_closed_maximal(itemsets, minimum_support=2)
print(f"- CLOSED ITEMSETS 2: {closed} \n")
print(f"- MAXIMAL ITEMSETS 2: {maximal} \n")

freq_itemsets = find_frequent(itemsets, minimum_support=2)
print(f"- FREQUENT ITEMSETS: {freq_itemsets} \n\n")


#################### COMPLICATED CASE ####################
print("COMPLICATED CASE \n")
dataset = [["apple", "banana", "orange", "tomato"],
           [1, 0, 0, 1],
           [0, 1, 1, 1],
           [1, 1, 0, 1],
           [0, 0, 0, 1],
           [0, 0, 0, 1],
           [1, 1, 1, 1],
           [0, 1, 0, 1],
           [0, 0, 1, 0]]

itemsets = fp_growth_algorithm(dataset)
print(f"- FREQUENT ITEMSETS: {itemsets.to_dict()} \n")

closed = find_closed(itemsets, minimum_support=2)
print(f"- CLOSED ITEMSETS: {closed} \n")

maximal = find_maximal(itemsets, minimum_support=2)
print(f"- MAXIMAL ITEMSETS: {maximal} \n")

closed, maximal = find_closed_maximal(itemsets, minimum_support=2)
print(f"- CLOSED ITEMSETS 2: {closed} \n")
print(f"- MAXIMAL ITEMSETS 2: {maximal} \n")

freq_itemsets = find_frequent(itemsets, minimum_support=2)
print(f"- FREQUENT ITEMSETS: {freq_itemsets} \n\n")


#################### WITH CONVERSIONS CASE ####################
print("WITH CONVERSIONS CASE \n")
dataset = [["apple", "tomato"],
           ["banana", "orange", "tomato"],
           ["apple", "banana", "tomato"],
           ["tomato"],
           ["tomato"],
           ["apple", "banana", "orange", "tomato"],
           ["banana", "tomato"],
           ["orange"]]

itemsets = fp_growth_algorithm(dataset)
print(f"- FREQUENT ITEMSETS: {itemsets.to_dict()} \n")

closed = find_closed(itemsets, minimum_support=2)
print(f"- CLOSED ITEMSETS: {closed} \n")

maximal = find_maximal(itemsets, minimum_support=2)
print(f"- MAXIMAL ITEMSETS: {maximal} \n")

closed, maximal = find_closed_maximal(itemsets, minimum_support=2)
print(f"- CLOSED ITEMSETS 2: {closed} \n")
print(f"- MAXIMAL ITEMSETS 2: {maximal} \n")

freq_itemsets = find_frequent(itemsets, minimum_support=2)
print(f"- FREQUENT ITEMSETS: {freq_itemsets} \n\n")