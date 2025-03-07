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
by adding nodes when a new element of an itemset appears and by taking into account the number of times a certain element appears in a data set. The latter is accomplished by assigning a counter, formally called **support**, on each of the nodes. This creates a compressed representation of the data set and it is more efficient than Apriori algorithm as it avoid scanning the data set multiple times.

<p align="center">
<img src="https://drive.google.com/uc?id=1n4JESI8Py7ZdowXbkXn5SQ9Jyyug5BZD" width="500">
</p>
<p align="center">
<i> FP tree example. Image taken from https://www.scaler.com/topics/data-mining-tutorial/fp-growth-in-data-mining/. </i>
</p>

After creating the FP tree, the maximal and closed frequent itemsets can be find by its definition. The **maximal frequent itemsets** are itemsets which are frequent, with a support above the threshold, and none of the immediate supersets are frequent. In contrast, **closed frequent itemsets** are itemsets that are frequent and its immediate supersets do not have the same support (they have an inferior support). An interesting property derived by this definition is that maximal itemsets are closed, but not viceversa. This fact can reduce the number of times needed to iterate over the tree while implementing the algorithm.

<p align="center">
<img src="https://drive.google.com/uc?id=1PKLofcteTMV7TZ7kjCB8MWQrOLt6EeOZ" width="500">
</p>
<p align="center">
<i> FP tree example with highlighted maximal and closed frequent itemsets. Image taken from https://www.geeksforgeeks.org/maximal-frequent-itemsets/. </i>
</p>

## Node class

The **Node** class is used to create the tree structure for the FP-Growth algorithm. It works by recursively generating child nodes from a root node using the *add_child* method. The class stores the node's value, a counter tracking the number of times the node has appeared, a list of child nodes, and a reference to its parent node.

The *itemset* method is crucial for implementing the algorithms that find closed and maximal frequent itemsets, as it enables to access recursively to the preceding nodes in a given tree branch.

For clarity, we provide a list of the attributes and methods of this class, followed by their descriptions:

- **Attributes**:
  - **value**: Type of item in the transaction.
  - **children**: List of immediate children of the node.
  - **counter**: The number of times the itemset has appeared.
  - **parent**: Reference to the parent node.
- **Methods**:
  - ***add_child()***: Adds a node to the list of children.
  - ***count()***: Increases the counter of the node by one.
  - ***itemset()***: Accesses the parent nodes to create a list of transactions.
  - ***to_dict()***: Converts the tree rooted at this node into a dictionary representation.

## Maximal and closed frequent itemsets finding

As previously said, the maximal and closed frequent itemsets were obtained by applying the definition and the facilities provide by the *Node* class. The implementation can be easily checked in *maximal_closed_itemsets.py* and in the following flowchart.

<p align="center">
<img src="https://drive.google.com/uc?id=1oTh8D-PztgOqgEVF6Hr03eByBpKFj4Le" width="450">
</p>
<p align="center">
<i> Flowchart of the algorithm used for finding the maximal and closed frequent itemsets.</i>
</p>

## How to use it
### Dependencies

This implementation do not need any external library. The version of Python used was 3.10.6.

### Search

Run *frequent_itemset_mining.py* to start the search of closed and maximal frequent itemsets in the Real Market Data for Association Rules data set.

### Results

The minimum support for considering an itemset as frequent is set as 40 by default. Running *frequent_itemset_mining.py* with this support shows the following results.

<p align="center">
<img src="https://drive.google.com/uc?id=13fEEYV-8p4daTyDLqKasfEbEiaL39zxZ" width="1000">
</p>
<p align="center">
<i> Output of frequent_itemset_mining.py.</i>
</p>
