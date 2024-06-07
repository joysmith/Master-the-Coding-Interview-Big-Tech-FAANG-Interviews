const managersArray = [2, 2, 4, 6, -1, 4, 4, 5];
const informTimeArray = [0, 0, 4, 0, 7, 3, 6, 0];

const numOfMinutes = function (n, headID, managers, informTime) {
  /* Create adjancency list empty array
    [
  0   []
  1   []
  2   []
  3   []
  4   []
  5   []
  6   []
  7   []
    ]
  */
  const adjList = managers.map(() => []);

  /* fill adjancency list
    [
  0   []
  1   []
  2   [0, 1]
  3   []
  4   [2, 5, 6]
  5   [7]
  6   [3]
  7   []
    ]
  */
  // employee 0 till number of total employee
  for (let employee = 0; employee < n; employee++) {
    // get manager of this current employee from manager array
    const manager = managers[employee];

    //check, if manager is head of company then skip this loop and move to next iteration
    if (manager === -1) continue;
    // add this manager to managee in adj list
    adjList[manager].push(employee);
  }

  return dfs(headID, adjList, informTime);
};

// currentId is starting employee
const dfs = function (currentId, adjList, informTime) {
  // base case, when employee has no subordinate
  if (adjList[currentId].length === 0) {
    return 0;
  }

  let max = 0;
  // get subordinate array from current Id
  const subordinates = adjList[currentId];
  // loop through every subordinate
  for (let i = 0; i < subordinates.length; i++) {
    // calculate time
    max = Math.max(max, dfs(subordinates[i], adjList, informTime));
  }

  return max + informTime[currentId];
};

console.log(numOfMinutes(8, 4, managersArray, informTimeArray));

// 13 min ans
