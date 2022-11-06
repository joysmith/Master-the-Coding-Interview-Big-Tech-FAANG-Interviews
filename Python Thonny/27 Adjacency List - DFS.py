# graph represented as adjacency list
adjacencyList = [
  [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2],
]

# recursive DFS
def traversalDFS(vertex, graph, values, seen):

    # store current vertex in values array
    values.append(vertex)
    # In dictionary make this current vertex visited
    seen[vertex] = True
    # get connected/neighbour vertices, to this current vertex stored inside adjacency list graph
    connections = graph[vertex]

    for i in range(len(connections)):
        # get the first connected vertex
        connection = connections[i]
        # check, have we visited/seen this vertex, In seen dictionary map
        # if we have not visited this vertex then do this
        if (not seen.get(connection)):
            # inset new connection vertex in traversalDFS fun, with all inputs
            traversalDFS(connection, graph, values, seen)


# value array to store traversal vertex
values = []

traversalDFS(0, adjacencyList, values, {})

print(values)
#(9) [0, 1, 3, 2, 8, 4, 6, 7, 5]
