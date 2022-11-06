// graph represented as adjacency matrix
const adjacencyMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0],
];

// recursive DFS
const traversalDFS = function (vertex, graph, values, seen) {
  // store current vertex in values array
  values.push(vertex);
  // In dictionary make this current vertex visited
  seen[vertex] = true;
  // get connected/neighbour vertices, to this current vertex stored inside adjacency list graph
  const connections = graph[vertex];

  for (let v = 0; v < connections.length; v++) {
    //check, if there is a vertex in inner-array AND the vertex is not inside the dictionary then
    //       list                dict
    if (connections[v] > 0 && !seen[v]) {
      // inset new connection vertex in traversalDFS fun, with all inputs
      traversalDFS(v, graph, values, seen);
    }
  }
};
// value array to store traversal vertex
const values = [];

traversalDFS(0, adjacencyMatrix, values, {});

console.log(values);
