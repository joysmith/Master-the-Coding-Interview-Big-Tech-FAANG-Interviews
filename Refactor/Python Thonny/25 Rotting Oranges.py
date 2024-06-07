testMatrix = [
  [2, 1, 1, 0, 0],
  [1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1],
  [0, 1, 0, 0, 1]
]

directions = [
  [-1, 0], #up
  [0, 1], #right
  [1, 0], #down
  [0, -1] #left
]

# constant to represent 2,1,0 for readiability
ROTTEN = 2
FRESH = 1
EMPTY = 0


def orangesRotting(matrix):
    # check test case, Is matrix is empty
    if(len(matrix) == 0): 
        return 0
    # queue to store rotten oranges coordinates, when doing sequential search
    queue = [] 
    # initialize fresh oranges to 0 
    freshOranges = 0
   
    # sequential traversal
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # check, do we encounter rotten orange
            if(matrix[row][col] == ROTTEN):
                # store the coordinates in queue
                queue.append([row, col])
      
            # check, Have we encounter fresh oranges
            if(matrix[row][col] == FRESH):
                # store in fresh orange counter
                freshOranges += 1
    
    # initialize minute counter
    minutes = 0
    
    # get queue size to track what ring or what step of rotting process we are at
    currentQueueSize =len(queue)
  
   # run BFS as long as the queue has some value
    while(len(queue) > 0):
        # check, is current queue size is 0
        if(currentQueueSize == 0):
            # reset queue size
            currentQueueSize = len(queue)
            # increase by 1 min, because that level of fresh oranges has been rotten
            minutes += 1

        # get the coordiante value from the queue of rotten orange
        currentOrange = queue.pop(0)
        # decrease Current queue size tracking by 1 because we pulled the value out of it
        currentQueueSize -= 1

        # get the current row coordinate
        row = currentOrange[0]
        # get the current col coordinate
        col = currentOrange[1]
    
        # 4 direction navigationl coordinates
        for i in range(len(directions)):
            # get current direction cooedinates
            currentDir = directions[i]

            # perform addition on row coordinates
            nextRow = row + currentDir[0]
            # perform addition on col coordinates
            nextCol = col + currentDir[1]
      
            if(
                nextRow < 0 or # row value is smaller than 0 size in outer array, i.e -1 then we are out of bound
                nextRow >= len(matrix) or # //row value is greater than the size of outer array then we are out of bound
                nextCol < 0 or # col value is smaller than 0 size in inner array, i.e -1 then we are out of bound
                nextCol >= len(matrix[0]) # col value is greater than the size of inner array then we are out of bound
                ):  
                # skip this current direction and repeat the direction loop for next direction
                continue
      
            # check, have we encounter fresh orange
            if (matrix[nextRow][nextCol] == FRESH):
                # turn the fresh orange to rotten orange
                matrix[nextRow][nextCol] = 2
                # decrease the number of fresh orange
                freshOranges -= 1
                # store the current coordinate to queue
                queue.append([nextRow, nextCol])
      
    
  
    # check test case, Is there any fresh oranges left in counter
    if(freshOranges != 0):
        return -1
  
    return minutes

print(orangesRotting(testMatrix))