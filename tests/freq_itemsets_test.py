"""
Tests for checking fp_growth functions.
"""


from algorithms import fp_growth_algorithm


#################### SIMPLE CASE ####################
print("SIMPLE CASE \n")
dataset = [["apple", "banana", "orange", "tomato"],
           [1, 0, 0, 1],
           [0, 1, 1, 1],
           [1, 1, 0, 1],
           [0, 0, 0, 1]]

freq_itemsets = fp_growth_algorithm(dataset)
print(f"- FREQUENT ITEMSETS: {freq_itemsets.to_dict()} \n\n")


#################### COMPLICATED CASE ####################
print("COMPLICATED CASE \n")
dataset = [["apple", "banana", "orange", "tomato"],
           [1, 0, 0, 1],
           [0, 1, 1, 1],
           [1, 1, 0, 1],
           [0, 0, 0, 1],
           [1, 1, 1, 1],
           [1, 0, 0, 1],
           [0, 1, 0, 1]]

freq_itemsets = fp_growth_algorithm(dataset)
print(f"- FREQUENT ITEMSETS: {freq_itemsets.to_dict()} \n\n")


#################### WITH CONVERSIONS CASE ####################
print("WITH CONVERSIONS CASE \n")
dataset = [["apple", "tomato"],
           ["banana", "orange", "tomato"],
           ["apple", "banana", "tomato"],
           ["tomato"]]

freq_itemsets = fp_growth_algorithm(dataset)
print(f"- FREQUENT ITEMSETS: {freq_itemsets.to_dict()} \n\n")