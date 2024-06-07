const string = "abccabb";

// Time: O(N^2);
// Space: O(N)

const lengthOfLongestSubstring = function (s) {
  // test case, if string length is 0 or 1
  if (s.length <= 1) return s.length;
  // string length counter
  let longest = 0;
  // how to create a left pointer
  for (let left = 0; left < s.length; left++) {
    // create a dict data model to strore the character we have seen
    let seenChars = {};
    // where to store the length of substring
    let currentLength = 0;
    // how to create a right pointer
    for (let right = left; right < s.length; right++) {
      // get the current character from string data model
      const currentChar = s[right];
      // check do the current char exist in dictioary if not do this
      if (!seenChars[currentChar]) {
        // increate substring length by 1
        currentLength++;
        // store the current char in seen dict.
        seenChars[currentChar] = true;
        // compare the length of previous string with new string
        longest = Math.max(longest, currentLength);
      } else {
        // default if char exist in seen dict then
        // break this right pointer for loop
        break;
      }
    }
  }

  return longest;
};

console.log(lengthOfLongestSubstring(string));
