def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}

    for i in range(length):
        item = weights[i]
        target = limit - item

        if target not in hash_table:
            hash_table[item] = i
        else:
            target_index = hash_table[target]
            return (i, target_index)
