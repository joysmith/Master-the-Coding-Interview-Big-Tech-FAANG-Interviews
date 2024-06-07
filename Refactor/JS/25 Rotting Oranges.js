const testMatrix = [
  [2, 1, 1, 0, 0],
  [1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1],
  [0, 1, 0, 0, 1],
];

const directions = [
  [-1, 0], //up
  [0, 1], //right
  [1, 0], //down
  [0, -1], //left
];

// constant to represent 2,1,0 for readiability
const ROTTEN = 2;
const FRESH = 1;
const EMPTY = 0;

const orangesRotting = function (matrix) {
  // check test case, Is matrix is empty
  if (matrix.length === 0) return 0;

  // queue to store rotten oranges coordinates, when doing sequential search
  const queue = [];
  // initialize fresh oranges to 0
  let freshOranges = 0;

  // sequential traversal
  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      // check, do we encounter rotten orange
      if (matrix[row][col] === ROTTEN) {
        // store the coordinates in queue
        queue.push([row, col]);
      }

      // check, Have we encounter fresh oranges
      if (matrix[row][col] === FRESH) {
        // store in fresh orange counter
        freshOranges++;
      }
    }
  }

  // initialize minute counter
  let minutes = 0;
  // get queue size to track what ring or what step of rotting process we are at
  let currentQueueSize = queue.length;

  // BFS as long as the queue has some value
  while (queue.length > 0) {
    // check, is current queue size is 0
    if (currentQueueSize === 0) {
      //  reset queue size
      currentQueueSize = queue.length;
      // increase by 1 min, because that level of fresh oranges has been rotten
      minutes++;
    }

    // get the coordiante value from the queue of rotten orange
    const currentOrange = queue.shift();
    // decrease Current queue size tracking by 1 because we pulled the value out of it
    currentQueueSize--;

    // get the current row coordinate
    const row = currentOrange[0];
    // get the current col coordinate
    const col = currentOrange[1];

    // 4 direction navigationl coordinates
    for (let i = 0; i < directions.length; i++) {
      // get current direction cooedinates
      const currentDir = directions[i];

      // perform addition on row coordinates
      const nextRow = row + currentDir[0];
      // perform addition on col coordinates
      const nextCol = col + currentDir[1];

      if (
        nextRow < 0 || //row value is smaller than 0 size in outer array, i.e -1 then we are out of bound
        nextRow >= matrix.length || //row value is greater than the size of outer array then we are out of bound
        nextCol < 0 || // col value is smaller than 0 size in inner array, i.e -1 then we are out of bound
        nextCol >= matrix[0].length // col value is greater than the size of inner array then we are out of bound
      ) {
        // skip this current direction and repeat the direction loop for next direction
        continue;
      }

      // check, have we encounter fresh orange
      if (matrix[nextRow][nextCol] === FRESH) {
        // turn the fresh orange to rotten orange
        matrix[nextRow][nextCol] = 2;
        // decrease the number of fresh orange
        freshOranges--;
        // store the current coordinate to queue
        queue.push([nextRow, nextCol]);
      }
    }
  }

  // check test case, Is there any fresh oranges left in counter
  if (freshOranges !== 0) {
    return -1;
  }

  return minutes;
};

console.log(orangesRotting(testMatrix));
