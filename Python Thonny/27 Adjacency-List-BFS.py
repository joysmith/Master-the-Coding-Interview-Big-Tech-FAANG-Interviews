# graph represented as adjacency list
adjacencyList = [
  [1, 3],       # 0
  [0],          # 1
  [3, 8],       # 2
  [0, 2, 4, 5], # 3
  [3, 6],       # 4
  [3],          # 5
  [4, 7],       # 6
  [6],          # 7
  [2]           # 8
]

# recursive BFS
def traversalBFS(graph):
    # dictionary to keep track on nodes we visited
    seen = {}
    #initialize queue from 0 node on graph
    queue = [0]
    # value array to store traversal
    values = []

    # run as long as there is node inside queue
    while(len(queue)):

        #const vertex = queue.shift(); JS code
        # get the current node/vertex from the queue array
        vertex = queue.pop(0)
        # store vertex visit value in value array
        values.append(vertex)
        # In dictionay make this node visited
        seen[vertex] = True

        # get connected/neighbouring nodes to this current node stored inside adjancey list graph
        connections = graph[vertex]

        # run as long as there are connecting nodes
        for i in range(len(connections)):
            # get the first connected node 
            connection = connections[i]

            # check, have we visited/seen this node before in seen dictionary map
            # if we have not visited this node then do this
            if(not seen.get(connection)):
                # add this node to queue array
                queue.append(connection) 

    return values


print(traversalBFS(adjacencyList))

#(9) [0, 1, 3, 2, 4, 5, 8, 6, 7]