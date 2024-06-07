const p = [
  [1, 0],
  [2, 1],
  [2, 5],
  [0, 3],
  [4, 3],
  [3, 5],
  [4, 5],
];

const canFinish = function (n, prerequisites) {
  // generate empty structure of adjancency list
  const adjList = new Array(n).fill(0).map(() => []);

  // fill adjancency list from preequisites list
  for (let i = 0; i < prerequisites.length; i++) {
    // get the pair from the prerequisites list
    const pair = prerequisites[i];

    // get the second value from the pair
    // and push first value from pair
    // inside adjlist
    // adjList[0].push(1);
    adjList[pair[1]].push(pair[0]);
  }

  for (let v = 0; v < n; v++) {
    // queue to store vertex
    const queue = [];
    // seen to track vertex we visited
    const seen = {};

    for (let i = 0; i < adjList[v].length; i++) {
      // push value from the adj list to queue
      queue.push(adjList[v][i]);
    }

    // BFS
    while (queue.length) {
      // get the current value from queue
      const current = queue.shift();
      // store this current value in seen object
      seen[current] = true;

      //Test case, check cycle
      if (current === v) return false;

      // get the current value
      const adjacent = adjList[current];

      //
      for (let i = 0; i < adjacent.length; i++) {
        // get the next value
        const next = adjacent[i];
        //check, as long we havent seen value before then,
        if (!seen[next]) {
          // store this in queue
          queue.push(next);
        }
      }
    }
  }

  return true;
};

console.log(canFinish(6, p));
