const testMatrix = [
  //  c0  c1  c2  c3  c4
  [1, 2, 3, 4, 5], // r0
  [6, 7, 8, 9, 10], // r1
  [11, 12, 13, 14, 15], // r2
  [16, 17, 18, 19, 20], // r3
];

//  grid[r0][c0]   grid[r0][c1]   grid[r0][c2]   grid[r0][c3]   grid[r0][c4]
//        1               2               3              4            5

//  grid[r1][c0]   grid[r1][c1]   grid[r1][c2]   grid[r1][c3]   grid[r1][c4]
//        6               7               8           9               10

//  grid[r2][c0]   grid[r2][c1]   grid[r2][c2]   grid[r2][c3]   grid[r2][c4]
//        11              12              13          14              15

//  grid[r3][c0]   grid[r3][c1]   grid[r3][c2]   grid[r3][c3]   grid[r3][c4]
//        16              17              18          19              20

const numberOfIslands = function (matrix) {
  // sequential traversal for row
  for (let row = 0; row < matrix.length; row++) {
    // sequential traversal for col
    for (let col = 0; col < matrix[0].length; col++) {
      // sequential traversal
      console.log(matrix[row][col]);
    }
  }
};

console.log(numberOfIslands(testMatrix));
