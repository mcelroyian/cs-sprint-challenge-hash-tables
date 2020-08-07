def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []
    total = len(arrays)
    for l in arrays:
        for n in l:
            if n not in d.keys():
                d[n] = 0
            d[n] += 1
            if d[n] == total:
                result.append(n)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
