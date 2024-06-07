const p = [
  [1, 0],
  [2, 1],
  [2, 5],
  [0, 3],
  [4, 3],
  [3, 5],
  [4, 5],
];

const canFinishWithAdj = function (n, prerequisites) {
  // generate empty structure of indegree list
  // and fill with 0 as initial value
  const inDegree = new Array(n).fill(0);

  // generate empty structure of adjancency list
  const adjList = inDegree.map(() => []);

  //filling adjlist, in-degree list using prerequisites array
  for (let i = 0; i < prerequisites.length; i++) {
    // get the current pair from adjlist
    const pair = prerequisites[i];

    // In indegree at pair at 0, increment
    // indegree-OUTERARRAY, Pair-INNERARRAY
    inDegree[pair[0]]++;

    // populate adjlist
    // adjList[1].push(0);
    // pair at 1, push in the value of pair at 0
    adjList[pair[1]].push(pair[0]);
  }

  // create stack for indegree with 0, vertex storing
  const stack = [];

  for (let i = 0; i < inDegree.length; i++) {
    // check, is indegree is equal to 0 at i i.e vertex), then
    if (inDegree[i] === 0) {
      // push index i.e vertex  into the stack
      stack.push(i);
    }
  }

  // to know how many vertex we processed
  let count = 0;

  while (stack.length) {
    // get current indegree vertex from stack
    const current = stack.pop();
    // increment the count for vertex
    count++;

    // give me the adjacent of current vertex from adjlist
    const adjacent = adjList[current];

    // loop through adjacent array
    for (let i = 0; i < adjacent.length; i++) {
      // get next adjacent vertex
      const next = adjacent[i];
      // reduce indegree value of vertex by 1
      inDegree[next]--;

      //check, is next indgree value is equal to 0, then
      if (inDegree[next] === 0) {
        // store into stack for process
        stack.push(next);
      }
    }
  }

  // check, for cycle:(T/F)
  return count === n;
};

canFinishWithAdj(6, p);
