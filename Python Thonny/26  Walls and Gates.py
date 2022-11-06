INF = 2147483647

testMatrix = [
  [INF, -1, 0, INF],
  [INF, INF, INF, 0],
  [INF, -1, INF, -1],
  [0, -1, INF, INF]
]

WALL = -1
GATE = 0
EMPTY = 2147483647
directions = [
  [-1, 0], #up
  [0, 1], #right
  [1, 0], #down
  [0, -1] #left
]

def dfs(grid, row, col, count):

    if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or count > grid[row][col]): 
        return
    
    grid[row][col] = count
    
    for i in range(len(directions)):
        currentDir = directions[i]
        dfs(grid, row + currentDir[0], col + currentDir[1], count + 1)
  



def wallsAndGates(rooms):

    for row in range(len(rooms)):
        for col in range(len(rooms)):

            if (rooms[row][col] == GATE): 
                dfs(rooms, row, col, 0)
    

wallsAndGates(testMatrix)

print(testMatrix)

#[ [ 3, -1, 0, 1 ], [ 2, 2, 1, 0 ], [ 1, -1, 2, -1 ], [ 0, -1, 3, 4 ] ]