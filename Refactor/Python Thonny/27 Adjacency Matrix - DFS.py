# graph represented as adjacency list
adjacencyMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],  # r0
  [1, 0, 0, 0, 0, 0, 0, 0, 0],  # r1
  [0, 0, 0, 1, 0, 0, 0, 0, 1],  # r2
  [1, 0, 1, 0, 1, 1, 0, 0, 0],  # r3
  [0, 0, 0, 1, 0, 0, 1, 0, 0],  # r4
  [0, 0, 0, 1, 0, 0, 0, 0, 0],  # r5
  [0, 0, 0, 0, 1, 0, 0, 1, 0],  # r6
  [0, 0, 0, 0, 0, 0, 1, 0, 0],  # r7
  [0, 0, 1, 0, 0, 0, 0, 0, 0],  # r8
]

def traversalDFS(vertex, graph, values, seen):

    # store current vertex in values array
    values.append(vertex)
    # In dictionary make this current vertex visited
    seen[vertex] = True
    # get connected/neighbour vertices, to this current vertex stored inside inside inner-array
    connections = graph[vertex]

    for v in range(len(connections)):
        #check, if there is a connecting vertex in inner-array AND the vertex is not inside the dictionary then
            #       list                dict
        if (connections[v] > 0 and not seen.get(v)):
            # inset new connection vertex in traversalDFS fun, with all inputs
            traversalDFS(v, graph, values, seen)
    
  

# value array to store traversal vertex
values = []

traversalDFS(0, adjacencyMatrix, values, {})

print(values)
