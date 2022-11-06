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

// recursive DFS
const traversalDFS = function (vertex, graph, values, seen) {
  // store current vertex in values array
  values.push(vertex);
  // In dictionary make this current vertex visited
  seen[vertex] = true;
  // get connected/neighbour vertices, to this current vertex stored inside adjacency list graph
  const connections = graph[vertex];

  for (let i = 0; i < connections.length; i++) {
    // get the first connected vertex
    const connection = connections[i];
    // check, have we visited/seen this vertex, In seen dictionary map
    // if we have not visited this vertex then do this
    if (!seen[connection]) {
      // inset new connection vertex in traversalDFS fun, with all inputs
      traversalDFS(connection, graph, values, seen);
    }
  }
};
// value array to store traversal vertex
const values = [];

traversalDFS(0, adjacencyList, values, {});

console.log(values);
//(9) [0, 1, 3, 2, 8, 4, 6, 7, 5]
