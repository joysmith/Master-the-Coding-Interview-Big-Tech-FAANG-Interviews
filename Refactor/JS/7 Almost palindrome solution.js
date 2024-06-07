const string = "poop";

var validPalindrome = function (s) {
  // create left pointer
  let start = 0;
  // create right pointer
  let end = s.length - 1;

  // run the pointer until they meet/overlap each other

  while (start < end) {
    // check, start and end, char are not same then,

    if (s[start] !== s[end]) {
      // skip one char from left

      return (
        // skip one char from left
        validSubPalindrome(s, start + 1, end) ||
        // skip one char from right
        validSubPalindrome(s, start, end - 1)
      );
    }
    // move left pointer

    start++;
    // move right pointer

    end--;
  }
  return true;
};

// fuction to check the string is valid palindrom

var validSubPalindrome = function (s, start, end) {
  // move left and right pointer until they meet eachother

  while (start < end) {
    // check, left and right poiter char are not same, then

    if (s[start] !== s[end]) {
      return false;
    }

    // move left pointer

    start++;

    // move right pointer

    end--;
  }
  return true;
};

console.log(validPalindrome(string));
