array = [5,3,1,6,4,2]
kToFind = 4

def swap(array, i, j):
  temp = array[i]
  array[i] = array[j]
  array[j] = temp


def getPartition(nums, left, right):

  pivotElement = nums[right]
  partitionIdx = left


#this line to be checkek
# for (let j = left; j < right; j++) { note: we are not iterating on array
# for (let i = 0; i < cars.length) { note:The len() function should only be used for iterable objects such as list, tuple, dictionary and string.
  
  for j in range(left, right):

    
    if (nums[j] <= pivotElement):
      swap(nums, partitionIdx, j)
      partitionIdx += 1
    
  
  swap(nums, partitionIdx, right)

  return partitionIdx


def quickSort(nums, left, right):  
  if(left < right):
    partitionIndex = getPartition(nums, left, right)

    quickSort(nums, left, partitionIndex - 1)
    quickSort(nums, partitionIndex + 1, right)
  


def findKthLargest(nums, k):
  indexToFind = len(nums) - k
  quickSort(nums, 0, len(nums) - 1)
  return nums[indexToFind]


print(findKthLargest(array, kToFind))
