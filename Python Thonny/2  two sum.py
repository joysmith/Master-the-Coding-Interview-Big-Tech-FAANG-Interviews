numsArray = [1, 3, 7, 9, 2]
targetToFind = 11

def findTwoSum(nums, target):
    
    # how to create p1 pointer
    for p1 in range(len(nums)):
        # using p1 pointer in nums data-model
        numberToFind = target - nums[p1]
        
        # how to create p2 pointer and using in nums data-model
        # for (let p2 = p1 + 1; p2 < nums.length; p2++) {  --JS code
        #         startValue  endValue
        for p2 in range(p1+1, len(nums)): 
            # check number to find do exist in nums data-model,then
            if(numberToFind == nums[p2]):
                return [p1, p2]                      

    # test case
    return None   
          
    
print(findTwoSum(numsArray, targetToFind))
