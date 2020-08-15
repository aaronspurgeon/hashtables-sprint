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
    Ticket = {}
    route = []

    for i in tickets:
        Ticket[i.source] = i.destination

    for j in range(length):
        if not route:
            route.append(Ticket['NONE'])
        else:
            route.append(Ticket[route[-1]])

    return route
