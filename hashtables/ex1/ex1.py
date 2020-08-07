def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if length == 0:
        return None
    # Your code here
    h = {}
    #build hash
    for i in range(length):
        num = weights[i]
        diff = limit - num
        if diff in h.keys():
            return (i,h[diff])
        h[num] = i
    return None

