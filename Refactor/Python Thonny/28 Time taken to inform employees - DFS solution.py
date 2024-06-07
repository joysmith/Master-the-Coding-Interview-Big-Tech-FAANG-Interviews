managersArray = [2, 2, 4, 6, -1, 4, 4, 5]
informTimeArray = [0, 0, 4, 0, 7, 3, 6, 0]


def numOfMinutes(n, headID, managers, informTime):
    # Create adjancency list empty array
    #   [
    # 0   []
    # 1   []
    # 2   []
    # 3   []
    # 4   []
    # 5   []
    # 6   []
    # 7   []
    #   ]
    # const adjList = managers.map(() => []);   JS code
    adjList = list(map(lambda i : [] , managersArray))


    # fill adjancency list
        #   [
    # 0   []
    # 1   []
    # 2   [0, 1]
    # 3   []
    # 4   [2, 5, 6]
    # 5   [7]
    # 6   [3]
    # 7   []
    #   ] 
    #   initial     end excluding last value: employee < n
    # employee 0 till number of total employee
    for employee in range(n): 
        #(let employee = 0; employee < n; employee++):
        #     initial       condition       increment

        # get manager of this current employee from manager array
        manager = managers[employee]

        # check, if manager is head of company then skip this loop and move to next iteration
        if (manager == -1):
            continue

        # add this manager to managee in adj list
        adjList[manager].append(employee)
  

    return dfs(headID, adjList, informTime)


# currentId is starting employee
def dfs(currentId, adjList, informTime):

    # base case, when employee has no subordinate
    if (len(adjList[currentId]) == 0):
        return 0
  

    maximum = 0
    # get subordinate array from current Id
    subordinates = adjList[currentId]
    # loop through every subordinate
    for i in range(len(subordinates)):
        # calculate time
        maximum = max(maximum, dfs(subordinates[i], adjList, informTime))


    return maximum + informTime[currentId]


print(numOfMinutes(8, 4, managersArray, informTimeArray))

# 13 min ans
