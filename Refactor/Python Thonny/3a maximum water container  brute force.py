# heightsArray = [4, 8, 1, 2, 3, 9]

heightsArray = [7,1,2,3,9]

def getMaxWaterContainer(heights):
    # replacement updation
    maxArea = 0

    # how to create p1 pointer
    for p1 in range(len(heights)):
        # how to create p2 pointer
        for p2 in range(p1+1, len(heights)):
            # get the minimum height between two walls
            height = min(heights[p1], heights[p2])
            # get the width between two walls
            width = p2 - p1
            # calulate area
            area = height * width
            # replace max area value by comparing with old one
            maxArea = max(maxArea, area)

    return maxArea   
          
    
print(getMaxWaterContainer(heightsArray))
