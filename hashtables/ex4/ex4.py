def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result = []

    for i in a:
        if i != 0:
            hash_table[i] = 1
            if -i in hash_table:
                result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
