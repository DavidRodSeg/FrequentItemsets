"""
Functions for applying conversion operations to the data set.
"""

def one_hot_vector(feature):
    """
    Applies one-hot encoding to the input feature vector.

    Arguments:
        feature (list): The feature vector to encode using one-hot encoding.

    Returns:
        list: The feature vector with one-hot encoding applied.
    """
    one_hot = []
    elements = sorted(set(feature))
    if len(elements) == 2:
        one_hot = [1 if value == elements[0] else 0 for value in feature]
    else:
        for element in elements:
            one_hot.append([1 if value == element else 0 for value in feature])

    return one_hot


def one_hot_encoding(dataset):
    """
    Applies one-hot encoding to the input dataset.

    Arguments:
        dataset (list): The dataset to encode using one-hot encoding.

    Returns:
        list: The dataset with one-hot encoding applied.
    """
    one_hot = []
    tdataset = list(zip(*dataset))
    
    for feature in tdataset:
        one_hot.append(one_hot_vector(feature))
    one_hot = list(zip(*one_hot))

    return one_hot
    

def transaction_to_binary(transaction_data):
    """
    Converts a dataset in the transaction data format into a 
    binary array.

    Arguments:
        transaction_data (list): Dataset in the transaction data format. 
        Example: [['apple', 'banana', 'carrot'],['banana'],...]
    
    Returns:
        list: Dataset in the form of a binary array.
    """
    binary_data = []

    flattened_data = [data for row in transaction_data for data in row]
    header = sorted(set(flattened_data))
    # binary_data.append(header)

    for transaction in transaction_data:
        binary_row = [1 if item in transaction else 0 for item in header]
        binary_data.append(binary_row)

    return binary_data, header
