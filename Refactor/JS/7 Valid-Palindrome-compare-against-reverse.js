const string = "A man, a plan, a canal: Panama";

const isValidPalindrome = function (s) {
  // regix pattern
  s = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
  //  to store reverse string data model
  let rev = "";

  // generate a reverse string using a reverse for loop.
  for (let i = s.length - 1; i >= 0; i--) {
    rev += s[i];
  }
  // check, are both string same or not
  return rev === s;
};

console.log(isValidPalindrome(string));
