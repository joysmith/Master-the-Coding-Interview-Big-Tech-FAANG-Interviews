import numpy

testMatrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]

directions = [
  [-1, 0], #up
  [0, 1],  #right
  [1, 0],  #down
  [0, -1]  #left
]


def traversalBFS(matrix):
    # generate navigation tracking map data model and fill false  
    #JS code line
    #seen = new Array(matrix.length).fill(0).map(() => new Array(matrix[0].length).fill(false));
    seen = numpy.full((len(matrix),len(matrix[0])), False)

    #create array data model to store places we visit
    values = []

    #initialize with top left corner
    queue = [[0, 0]]

    while(len(queue)):
        #JS code line
        # const currentPos = queue.shift(); method remove first item from the queue FIFO
        #get first value from our queue data model
        currentPos = queue.pop(0)
        #get coordinates value of currentPos 
        row = currentPos[0]
        col = currentPos[1]
    
        #base condition to end recursive function if any cond is True
        #out of bound or Already visited in map
        if(row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]):
            continue #start while loop again
    
        # update navigation tracking map data model to True  
        seen[row][col] = True
        # add new navigated value to array data model
        values.append(matrix[row][col])
    

      #how to traverse in 4 direction using direction array data model
        for i in range(len(directions)):
            #take the first value from direction array 
            currentDir = directions[i]
            #perform addition on previous:row,col with currentDir:row,col   
            queue.append([row + currentDir[0], col + currentDir[1]])
    
    return values




print(traversalBFS(testMatrix))

#[1, 2, 5, 3, 6, 9, 4, 7, 10, 13, 8, 11, 14, 12, 15, 16]