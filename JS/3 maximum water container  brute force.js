const heightsArray = [4, 8, 1, 2, 3, 9];
// const heightsArray = [7,1,2,3,9];

const getMaxWaterContainer = function (heights) {
  // replacement updation
  let maxArea = 0;
  // how to create p1 pointer
  for (let p1 = 0; p1 < heights.length; p1++) {
    // how to create p2 pointer
    for (let p2 = p1 + 1; p2 < heights.length; p2++) {
      // get the minimum height between two walls
      const height = Math.min(heights[p1], heights[p2]);
      // get the width between two walls
      const width = p2 - p1;
      // calulate area
      const area = height * width;
      // replace max area value by comparing with old one

      maxArea = Math.max(maxArea, area);
    }
  }

  return maxArea;
};

console.log(getMaxWaterContainer(heightsArray));
