elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

def getTrappedRainwater(heights):

    # total updation
    totalWater = 0

    # how to create p pointer
    for p in range(len(heights)):
        # create leftP pointer from main p ponter
        leftP = p
        # create RightP pointer from main p ponter
        rightP = p
        # to store max left height
        maxLeft = 0 
        # to store max right height
        maxRight = 0


        # howt to use leftP pointer in array data model to move left direction
        # until it reaches to 0
        while(leftP >= 0):
            # get max height from left side
            maxLeft = max(maxLeft, heights[leftP])
            # move left pointer to left direction
            leftP -= 1

        # howt to use rightP pointer in array data model to move right direction
        # unitil it reaches to end of array
        while(rightP < len(heights)):
            # get max height from right side
            maxRight = max(maxRight, heights[rightP])
            # move right pointer to right direction
            rightP += 1

        # formaula to calculate current water 
        currentWater = min(maxLeft, maxRight) - heights[p]

        # check, that water is always in positive or above the base
        if(currentWater >= 0):
            # addition updation
            totalWater += currentWater

    return totalWater


print(getTrappedRainwater(elevationArray))
        