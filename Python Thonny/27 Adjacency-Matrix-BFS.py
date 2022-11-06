# graph represented as adjacency matrix
adjacencyMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],  #0
  [1, 0, 0, 0, 0, 0, 0, 0, 0],  #1
  [0, 0, 0, 1, 0, 0, 0, 0, 1],  #2
  [1, 0, 1, 0, 1, 1, 0, 0, 0],  #3
  [0, 0, 0, 1, 0, 0, 1, 0, 0],  #4
  [0, 0, 0, 1, 0, 0, 0, 0, 0],  #5
  [0, 0, 0, 0, 1, 0, 0, 1, 0],  #6
  [0, 0, 0, 0, 0, 0, 1, 0, 0],  #7
  [0, 0, 1, 0, 0, 0, 0, 0, 0]   #8
]

# recursive BFS
def traversalBFS(graph):
    # dictionary to keep track on nodes we visited
    seen = {}
    # initialize queue from 0 node on graph
    queue = [0]
    # value array to store traversal
    values = []

    # run as long as there is node inside queue
    while(len(queue)):
        #const vertex = queue.shift();  JS code
        # get the current vertex from the queue array
        vertex = queue.pop(0)
        # store current vertex visit value in value array
        values.append(vertex)
        # In dictionay make this vertex visited
        seen[vertex] = True

        # get connected/neighbouring nodes to this current node stored inside inner-array
        connections = graph[vertex]

        # run as long as there are connecting nodes
        for v in range(len(connections)):
            #if(connections[v] > 0 && !seen[v]) {   JS code
            #check, if there is a connecting vertex in inner-array AND the vertex is not inside the dictionary then
            #       list                dict    
            if(connections[v] > 0 and  not seen.get(v)):
                # add this node to queue array
                queue.append(v)
      
    return values

print(traversalBFS(adjacencyMatrix))


#(9) [0, 1, 3, 2, 4, 5, 8, 6, 7]