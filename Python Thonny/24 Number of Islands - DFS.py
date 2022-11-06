testMatrix = [
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 1, 1, 0],
  [1, 0, 1, 0, 1]
]

directions = [
  [-1, 0], #up
  [0, 1], #right
  [1, 0], #down
  [0, -1] #left
]

def dfs(grid, currentRow, currentCol):

    if(currentRow < 0 or currentRow >= len(grid) or currentCol < 0 or currentCol >= len(grid[0])):
        return

    if(grid[currentRow][currentCol] == 1):
        grid[currentRow][currentCol] = 0

        for i in range(len(directions)):
            currentDir = directions[i]
            row = currentDir[0]
            col = currentDir[1]
            dfs(grid, currentRow + row, currentCol + col)
        
  


def numberOfIslands(grid):

    if(not len(grid)):
        return 0
  
    islandCount = 0;
  
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == 1):
                islandCount += 1
                dfs(grid, row, col)
      
    return islandCount



print(numberOfIslands(testMatrix))