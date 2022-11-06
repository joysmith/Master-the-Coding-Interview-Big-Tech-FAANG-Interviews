const numsArray = [1, 3, 7, 9, 2];
const targetToFind = 11;

const findTwoSum = function (nums, target) {
  // how to create p1 pointer
  for (let p1 = 0; p1 < nums.length; p1++) {
    // using p1 pointer in nums data-model
    const numberToFind = target - nums[p1];
    // how to create p2 pointer and using in nums data-model
    for (let p2 = p1 + 1; p2 < nums.length; p2++) {
      // check number to find do exist in nums data-model,then
      if (numberToFind === nums[p2]) {
        return [p1, p2];
      }
    }
  }

  // test case
  return null;
};

console.log(findTwoSum(numsArray, targetToFind));
