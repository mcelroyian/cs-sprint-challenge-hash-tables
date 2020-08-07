def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {}
    result = []
    # Your code here
    #look at each number
    for num in a:
        if num == 0:
            continue
        #add to hash
        if num not in d.keys():
            d[num] = True
        #check it inverse value exists
        if -num in d.keys():
            #if yes, add to results
            if d[num] and d[-num]:
                result.append(abs(num))
                d[num] = False
                d[-num] = False
            #if no continue
    return result


if __name__ == "__main__":

    print(has_negatives([1]))
