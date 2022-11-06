const string1 = "ab#z";
const string2 = "az#z";

//function to create string data model without #-tag
const buildString = function (string) {
  // create a list data model
  const builtString = [];

  // how to create a p pointer for traversal in string data model
  for (let p = 0; p < string.length; p++) {
    // check, element is not #, then
    if (string[p] !== "#") {
      //  add this element to our list data model
      builtString.push(string[p]);
    } else {
      // default case, element is equal to #, then
      // remove the last element from our list data model
      builtString.pop();
    }
  }

  return builtString;
};

// function to compare string data model
var backspaceCompare = function (S, T) {
  // get string without #-tag

  const finalS = buildString(S);

  // get string without #-tag
  const finalT = buildString(T);

  // check, if length of two string data model are not equal, then
  if (finalS.length !== finalT.length) {
    return false;
  } else {
    // default, if length of two string data model are equal, then

    // create p pointer
    for (let p = 0; p < finalS.length; p++) {
      // check, if elements in both string data model are not equal
      if (finalS[p] !== finalT[p]) {
        return false;
      }
    }
  }

  return true;
};

console.log(backspaceCompare(string1, string2));
