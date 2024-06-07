elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]



# 1. Identify the pointer with the lesser value
# 2. Is this pointer value greater than or equal to max on that side
#   yes -> update max on that side
#   no -> get water for pointer, add to total
# 3. move pointer inwards
# 4. repeat for other pointer
 


def getTrappedRainwater(heights):

    totalWater = 0
    left = 0
    right = len(heights) -1
    maxLeft = 0 
    maxRight = 0


# this while just is just gonna iterate over the  pointers until our pointer touch each other
    while(left < right):
# this if condition decides whether or not we are going to operate on the left pointer or the right pointer
#  by deciding which one is smaller
        if heights[left] <= heights[right]:
# this if condition then decide ok if we are operating the left one becuse the left is smaller
# then we've got to decide are we going to update the max or are we going to calculate for water
            if heights[left] >= maxLeft:
                maxLeft = heights[left]
            else:
                totalWater += maxLeft - heights[left]

            left += 1

        else:
# same are above for right side 
            if heights[right] >= maxRight:

                maxRight = heights[right]
            else:
                totalWater += maxRight - heights[right]
              
            right -= 1

    return totalWater


print(getTrappedRainwater(elevationArray))
        