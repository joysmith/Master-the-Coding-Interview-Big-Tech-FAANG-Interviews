const string = "{()[]}";
// create hash table data model
const parens = {
  "(": ")",
  "{": "}",
  "[": "]",
};

var isValid = function (s) {
  // test case: Is input is empty string
  if (s.length === 0) return true;
  // initialize stack data model using array
  const stack = [];
  //for loop to iterate our string
  for (let i = 0; i < s.length; i++) {
    // Is left bracket is stored in Hash table data model
    if (parens[s[i]]) {
      // store, left bracket in stack data model
      stack.push(s[i]);
    } else {
      // remove, left bracket from stack data model
      const leftBracket = stack.pop();
      // retrive, value of leftBrakcet from hash table data model
      const correctBracket = parens[leftBracket];
      // does left bracket is not equal to left bracket
      if (s[i] !== correctBracket) return false;
    }
  }
  // Is stack is empty
  return stack.length === 0;
};

console.log(isValid(string));
