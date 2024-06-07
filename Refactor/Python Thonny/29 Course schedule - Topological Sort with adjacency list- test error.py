p = [
  [1, 0],
  [2, 1],
  [2, 5],
  [0, 3],
  [4, 3],
  [3, 5],
  [4, 5],
]

def canFinishWithAdj(n, prerequisites):

    # generate empty structure of indegree list
    # and fill with 0 as initial value
    # const inDegree = new Array(n).fill(0); JS code
    inDegree = list(map(lambda i : [0] , [None] * n))

    # generate empty structure of adjancency list
    # const adjList = inDegree.map(() => []); JS code
    adjList = list(map(lambda i : [] , [None] * n))

    # filling adjlist, in-degree list using prerequisites array
    for i in range(len(prerequisites)):
        # get the current pair from adjlist
        pair = prerequisites[i]
        


        # In indegree at pair at 0, increment
        # indegree-OUTERARRAY, Pair-INNERARRAY x = x+1, result = my_list[0] + 3
        inDegree[pair[0]] += 1 
        
        # populate adjlist
        # adjList[1].push(0);
        # pair at 1, push in the value of pair at 0
        adjList[pair[1]].append(pair[0])
  

    # create stack for indegree with 0, vertex storing
    stack = []

    for i in range(len(inDegree)):
        # check, is indegree is equal to 0 at i i.e vertex), then
        if (inDegree[i] == 0):
            # push index i.e vertex  into the stack
            stack.append(i)
    
  

    # to know how many vertex we processed
    count = 0

    while (len(stack)):
        # get current indegree vertex from stack
        current = stack.pop()
        # increment the count for vertex
        count += 1

        # give me the adjacent of current vertex from adjlist
        adjacent = adjList[current]

        # loop through adjacent array
        for i in range(len(adjacent)):
            # get next adjacent vertex
            next = adjacent[i]
            # reduce indegree value of vertex by 1
            inDegree[next] -= 1

            # check, is next indgree value is equal to 0, then
            if (inDegree[next] == 0):
                # store into stack for process
                stack.push(next)
      
    
  

    #check, for cycle:(T/F)
    return count == n


print(canFinishWithAdj(6, p))
