const testMatrix = [
  [1, 1, 1, 0, 0],
  [1, 1, 1, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
];

const directions = [
  [-1, 0], //up
  [0, 1], //right
  [1, 0], //down
  [0, -1], //left
];

const numberOfIslands = function (matrix) {
  //check, Is matrix length is 0
  if (matrix.length === 0) return 0;

  // Island counter
  let islandCount = 0;

  // sequential search for row
  for (let row = 0; row < matrix.length; row++) {
    // sequential search for col
    for (let col = 0; col < matrix[0].length; col++) {
      // check, coordinate have we encounter 1 i.e island
      if (matrix[row][col] === 1) {
        // increase island count by 1
        islandCount++;
        // flip the value of coordinate in matrix
        matrix[row][col] = 0;
        // create queue data model for BFS
        const queue = [];
        // store row, col coordinate in queue
        queue.push([row, col]);

        // if there is value inside queue then
        while (queue.length) {
          // get the next value from queue that i need to process
          const currentPos = queue.shift();
          // get the row coordinate
          const currentRow = currentPos[0];
          // get the col coordinate
          const currentCol = currentPos[1];

          // navigation on 4 direction
          for (let i = 0; i < directions.length; i++) {
            // get the current moving direction
            const currentDir = directions[i];
            // perform addition to move next row
            const nextRow = currentRow + currentDir[0];
            // perform addition to move next col
            const nextCol = currentCol + currentDir[1];

            // check all bound of matrix
            if (
              nextRow < 0 ||
              nextRow >= matrix.length ||
              nextCol < 0 ||
              nextCol >= matrix[0].length
            ) {
              // break the current iteration from this direction move to next iteration
              continue;
            }

            // if value has 1 i.e island in current direction
            if (matrix[nextRow][nextCol] === 1) {
              // store this island coordiante to queue
              queue.push([nextRow, nextCol]);
              // flip this 1 i.e isalnd to 0
              matrix[nextRow][nextCol] = 0;
            }
          }
        }
      }
    }
  }

  return islandCount;
};

console.log(numberOfIslands(testMatrix));
