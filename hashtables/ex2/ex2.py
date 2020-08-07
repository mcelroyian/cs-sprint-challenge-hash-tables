#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    d = {}

    for t in tickets:
        d[t.source] = t.destination
    
    hops = 0
    city = "NONE"
    while hops < length:
        city = d[city]
        route.append(city)
        hops += 1
    print(route)
    return route
