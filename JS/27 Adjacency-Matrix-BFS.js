// graph represented as adjacency matrix
const adjacencyMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0], // 0
  [1, 0, 0, 0, 0, 0, 0, 0, 0], // 1
  [0, 0, 0, 1, 0, 0, 0, 0, 1], // 2
  [1, 0, 1, 0, 1, 1, 0, 0, 0], // 3
  [0, 0, 0, 1, 0, 0, 1, 0, 0], // 4
  [0, 0, 0, 1, 0, 0, 0, 0, 0], // 5
  [0, 0, 0, 0, 1, 0, 0, 1, 0], // 6
  [0, 0, 0, 0, 0, 0, 1, 0, 0], // 7
  [0, 0, 1, 0, 0, 0, 0, 0, 0], // 8
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
    // get the current vertex from the queue array
    const vertex = queue.shift();
    // store current vertex visit value in value array
    values.push(vertex);
    // In dictionay make this vertex visited
    seen[vertex] = true;

    // get connected/neighbouring nodes to this current node stored inside inner array
    const connections = graph[vertex];

    // run as long as there are connecting nodes
    for (let v = 0; v < connections.length; v++) {
      //       list                dict
      //check, if there is a vertex in inner-array AND the vertex is not inside the dictionary then
      if (connections[v] > 0 && !seen[v]) {
        // add this node to queue array
        queue.push(v);
      }
    }
  }

  return values;
};

console.log(traversalBFS(adjacencyMatrix));
