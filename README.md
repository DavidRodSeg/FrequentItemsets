# FrequentItemsets
## Objective
The goal of this project was to develop an algorithm for determining the frequency of itemsets in a given dataset and classifying them as either maximal or closed frequent itemsets.
Itemset generation was accomplished using the FP-Growth algorithm on a dataset in binary or transactional form. The resulting itemsets were stored in a tree structure implemented with a Node class.
The final solutions can be presented as a Python dictionary.

## Data set analysis
The data set used was [Real Market Data for Association Rules](https://www.kaggle.com/datasets/rukenmissonnier/real-market-data) which consists in a series of transactions in the form of a binary array, with "1" denoting
the presence of the product in the transaction and "0" the abscence of it. While the rows represents the transactions of a given customer, the columns represent the elements in those transactions.

## FP-Growth algorithm. Maximal and closed frequent itemsets
FP-Growth is an algorithm desing for finding frequent patterns in a data base or large data sets. The idea behind this algorihtm is to build a compressed representation of the data set in the form of a *FP tree*
by adding nodes when a new element of an itemset appears and by taking into account the number of times a certain element appears in a data set. The latter is accomplished by assigning a counter, formally called **support**
on each of the nodes. This creates a compressed representation of the data set and it is more efficient than Apriori algorithm as it avoid scanning the data set multiple times.

<p align="center">
<img src="https://drive.google.com/uc?id=1n4JESI8Py7ZdowXbkXn5SQ9Jyyug5BZD" width="500">
</p>
<p align="center">
<i> FP tree example. Image taken from https://www.scaler.com/topics/data-mining-tutorial/fp-growth-in-data-mining/. </i>
</p>

After creating the FP tree the maximal and closed frequent itemsets can be find 

## Node class

## How to use it
### Results

## References
