testMatrix = [
  [1, 1, 1, 0, 0],
  [1, 1, 1, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1]
]


directions = [
  [-1, 0], #up
  [0, 1], #right
  [1, 0], #down
  [0, -1] #left
]

def numberOfIslands(matrix):
    #check, Is matrix length is 0
    if(len(matrix) == 0): return 0
    
    #Island counter
    islandCount = 0

    #sequential search for row
    for row in range(len(matrix)):
        #sequential search for col
        for col in range(len(matrix[0])):

            #check, coordinate have we encounter 1 i.e island
            if(matrix[row][col] == 1):
                #increase island count by 1
                islandCount += 1
                #flip the value of coordinate in matrix
                matrix[row][col] = 0
                #create queue data model for BFS
                queue = []
                #store row, col coordinate in queue
                queue.append([row, col])

                #if there is value inside queue then
                while(len(queue)):
                    #  JS shift function replaced with pop(0)
                    # get the next value from queue that i need to process
                    currentPos = queue.pop(0)
                    # get the row coordinate
                    currentRow = currentPos[0]
                    # get the col coordinate
                    currentCol = currentPos[1]
                    
                    #navigation on 4 direction
                    for i in range(len(directions)):
                        #get the current moving direction
                        currentDir = directions[i]
                        # perform addition to move next row
                        nextRow = currentRow + currentDir[0]
                        # perform addition to move next col
                        nextCol = currentCol + currentDir[1]

                        #check all bound of matrix 
                        if(nextRow < 0 or nextRow >= len(matrix) or nextCol < 0 or nextCol >= len(matrix[0])):
                            #break the current iteration from this direction move to next iteration 
                            continue
                        
                        #if value has 1 i.e island in current direction
                        if(matrix[nextRow][nextCol] == 1):
                            #store this island coordiante to queue
                            queue.append([nextRow, nextCol])
                            #flip this 1 i.e isalnd to 0  
                            matrix[nextRow][nextCol] = 0
              
    return islandCount


print(numberOfIslands(testMatrix2))