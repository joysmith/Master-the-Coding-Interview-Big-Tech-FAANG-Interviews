// graph represented as adjacency list
const adjacencyList = [
  [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2],
];

// recursive BFS
const traversalBFS = function (graph) {
  // dictionary to keep track on nodes we visited
  const seen = {};
  // initialize queue from 0 node on graph
  const queue = [0];
  // value array to store traversal
  const values = [];

  // run as long as there is node inside queue
  while (queue.length) {
    // get the first node/vertex from the queue array
    const vertex = queue.shift();
    // store node/vertex visit value in value array
    values.push(vertex);
    // In dictionay make this current node visited
    seen[vertex] = true;

    // get connected/neighbouring nodes to this current node
    // stored inside adjancey list graph
    const connections = graph[vertex];

    // run as long as there are connecting nodes
    for (let i = 0; i < connections.length; i++) {
      // get the first connected node
      const connection = connections[i];

      // check, have we visited/seen this node before in seen dictionary map
      // if we have not visited this node then do this
      if (!seen[connection]) {
        // add this node to queue array
        queue.push(connection);
      }
    }
  }

  return values;
};

console.log(traversalBFS(adjacencyList));
