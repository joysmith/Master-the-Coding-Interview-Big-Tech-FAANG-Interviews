const elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2];

const getTrappedRainwater = function (heights) {
  // total updation
  let totalWater = 0;

  //how to create p pointer
  for (let p = 0; p < heights.length; p++) {
    // create leftP pointer from main p ponter
    let leftP = p,
      // create RightP pointer from main p ponter
      rightP = p,
      //  to store max left height
      maxLeft = 0,
      // to store max right height
      maxRight = 0;

    // howt to use leftP pointer in array data model to move left direction
    // until it reaches to 0
    while (leftP >= 0) {
      // get max height from left side
      maxLeft = Math.max(maxLeft, heights[leftP]);
      // move left pointer to left direction
      leftP--;
    }

    // howt to use rightP pointer in array data model to move right direction
    // unitil it reaches to end of array
    while (rightP < heights.length) {
      // get max height from right side
      maxRight = Math.max(maxRight, heights[rightP]);
      // move right pointer to right direction
      rightP++;
    }

    // formaula to calculate current water
    const currentWater = Math.min(maxLeft, maxRight) - heights[p];

    // check, that water is always in positive or above the base
    if (currentWater >= 0) {
      // addition updation
      totalWater += currentWater;
    }
  }

  return totalWater;
};

console.log(getTrappedRainwater(elevationArray));
