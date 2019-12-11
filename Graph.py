def checkNode(node, graph):
    '''Checks whether a node is in a graph'''
    if node in graph:
        return (True)
    else:
        return (False)


def fromLinks(links):
    '''
    Takes a list of links in the form of tuples, or lists,
    with two elements describing the connected nodes and returns a graph in the form of a dictionary.

    Exampple input: [(1,2),(1,4),(2,3),(3,4)] or [[1,2],[1,4],(,3),(3,4)]

    Example output (fm input): {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
    '''
    ## set up an empty dictionary
    graph = {}
    ##iterate thru the input nodes
    for link in links:
        ##Check if each node is in the graph, if it isnt add it.
        for node in link:
            if not checkNode(node, graph):
                graph[node] = []
        ##for both ends of the node add the link to the other
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    return graph


##tests

assert (fromLinks([(1, 2), (1, 4), (2, 3), (3, 4)]) == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
assert (fromLinks([[1, 2], [1, 4], [2, 3], [3, 4]]) == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
## these should run without error,
