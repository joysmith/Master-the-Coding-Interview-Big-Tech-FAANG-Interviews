heightsArray = [7,1,2,3,9]

def getMaxWaterContainer(heights):
    p1 = 0 
    p2 = len(heights) - 1 
    maxArea = 0


    while(p1 < p2):

        height = min(heights[p1], heights[p2])
        width = p2 - p1
        area = height * width
        maxArea = max(maxArea, area)
    
        if(heights[p1] <= heights[p2]):
            p1 += 1
        else:
            p2 -= 1
    
        return maxArea
             
    
print(getMaxWaterContainer(heightsArray))
