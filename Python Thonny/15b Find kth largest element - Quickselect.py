#array = [5,3,1,6,4,2]
array = [5,9,1,6,4,2]

kToFind = 4

def swap(array, i, j):
  temp = array[i]
  array[i] = array[j]
  array[j] = temp


def getPartition(nums, left, right):
  i = left

#this line of code to be seen
  #for (let j = left; j <= right; j++) {
  for j in range(left, right + 1):
    if (nums[j] <= nums[right]):
      swap(nums, i, j)
      i += 1
    
  
  return i - 1


def quickSelect(nums, left, right, indexToFind):
  partitionIndex = getPartition(nums, left, right)

  if (partitionIndex == indexToFind):
    return nums[partitionIndex]
  elif (indexToFind < partitionIndex):
    return quickSelect(nums, left, partitionIndex - 1, indexToFind)
  else:
    return quickSelect(nums, partitionIndex + 1, right, indexToFind)
  


def findKthLargest(nums, k):
  indexToFind = len(nums) - k

  return quickSelect(nums, 0, len(nums) - 1, indexToFind)


print(findKthLargest(array, kToFind))