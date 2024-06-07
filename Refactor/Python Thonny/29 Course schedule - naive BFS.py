p = [
     [1, 0], 
     [2, 1], 
     [2, 5], 
     [0, 3], 
     [4, 3], 
     [3, 5], 
     [4, 5]
    ]

def canFinish(n, prerequisites):
    #  generate empty structure of adjancency list
    adjList = list(map(lambda i : [] , [None] * n))
    #adjList = new Array(n).fill(0).map(() => []) JS code
  

  # fill adjancency list from preequisites list
    for i in range(len(prerequisites)):
        # get the pair from the prerequisites list
        pair = prerequisites[i]

        # get the second value from the pair
        # and push first value from pair
        # inside adjlist
        # adjList[0].push(1);
        adjList[pair[1]].append(pair[0])
  

    for v in range(n):
        # queue to store vertex
        queue = []
        # seen dictionary to track vertex we visited
        seen = {}

        for i in range(len(adjList[v])):
            # push value from the adj list to queue
            queue.append(adjList[v][i])
    
        #  BFS
        while(len(queue)):
            # get the current value from queue
            # const current = queue.shift();
            current = queue.pop(0)
            # store this current value in seen dictionary
            seen[current] = True

            # Test case, check cycle
            if(current == v):
                return False

            # get the current value
            adjacent = adjList[current]
        
            for i in range(len(adjacent)):   
                # get the next value   
                next = adjacent[i]
                # check, as long we havent seen value before then,
                if(not seen.get(next)):
                    # store this in queue
                    queue.append(next)
    
    return True


print(canFinish(6, p))
