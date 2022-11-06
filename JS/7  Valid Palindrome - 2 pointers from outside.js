const string = "A man, a plan, a canal: Panama";

const isValidPalindrome = function (s) {
  // regix pattern
  s = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();

  // initialize left/right pointers at start and end of string respectively
  let left = 0;
  right = s.length - 1;

  // loop through string characters while comparing them, then move the pointers closer to the center
  while (left < right) {
    // check, if left and right char are not same, then
    if (s[left] !== s[right]) {
      return false;
    }
    //  move left pointer
    left++;
    // move right pointer
    right--;
  }

  return true;
};

console.log(isValidPalindrome(string));
