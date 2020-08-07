def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if length == 0:
        return None
    # Your code here
    h = {}
    r = []
    #build hash
    for i in range(length):
        if weights[i] not in h:
            h[weights[i]] = {"d": False, "value": i}
        else:
            h[weights[i]] = {"d": True, "value": i}
    #loop through array checking if the diff num exists
    #check if another key exists as diff.
    for i in range(length):
        print(weights[i])
        diff = limit - i
        if diff == i and h[i]["d"]:
            r.append(i)
            r.append(h[i]["value"])
            print(r)
            return tuple(r.sort())
        if diff in h.keys():
            r.append(h[i]["value"])
            r.append(h[diff]["value"])
            print(r)
            return tuple(r.sort(reverse=True))
        #if yes add the two indexes to result
    #if reach end, result is None. return
    print(h)
    print(r)
    if not r:
        return None
