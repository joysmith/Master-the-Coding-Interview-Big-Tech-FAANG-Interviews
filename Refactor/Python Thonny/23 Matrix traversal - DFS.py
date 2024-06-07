import numpy

testMatrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
]

directions = [
  [-1, 0], #up
  [0, 1],  #right
  [1, 0],  #down
  [0, -1]  #left
]

def traversalDFS(matrix):
    # generate navigation tracking map data model and fill false  
    #JS code line
    #seen = new Array(matrix.length).fill(0).map(() => new Array(matrix[0].length).fill(false));
    seen = numpy.full((len(matrix),len(matrix[0])), False)

    #create array data model to store places we visit
    values = []

    dfs(matrix, 0, 0, seen, values)

    return values


def dfs(matrix, row, col, seen, values):

    #base condition to end recursive function if any cond is True
    if(row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col]): 
      return
  
    # update navigation tracking map data model to True  
    seen[row][col] = True
    # add new navigated value to array data model
    values.append(matrix[row][col])

  #how to traverse in 4 direction using direction array data model
    for i in range(len(directions)):
      #take the first value from direction array 
        currentDir = directions[i]
        #perform addition on previous:row,col with currentDir:row,col   
        dfs(matrix, row + currentDir[0], col + currentDir[1], seen, values)
  
print(traversalDFS(testMatrix))