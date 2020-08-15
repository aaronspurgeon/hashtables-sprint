def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    results = []
    hash_table = {}
    new_list = [j for i in arrays for j in i]
    for i in new_list:
        if i not in hash_table:
            hash_table[i] = 1
        else:
            hash_table[i] += 1
    for j in hash_table:
        if hash_table[j] > 1:
            results.append(j)
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
# print(intersection([
#     [1, 2, 3],
#     [1, 4, 5]]))
