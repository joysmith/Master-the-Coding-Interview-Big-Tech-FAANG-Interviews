const string1 = "(ab(cd)";

const minRemoveToMakeValid = function (str) {
  // convert string into array
  const res = str.split("");
  const stack = [];

  //initialize stack data model using array
  for (let i = 0; i < res.length; i++) {
    // check if we see the left bracket
    if (res[i] === "(") {
      // store, bracket in the stack data model
      stack.push(i);

      //check if we see the right bracket and stack has value inside of it
    } else if (res[i] === ")" && stack.length) {
      // remove, the last bracket from stack
      stack.pop();

      // check if we see the right bracket
    } else if (res[i] === ")") {
      // update the value of that character to be empty string
      res[i] = "";
    }
  }

  // if stach has value inside of data model
  while (stack.length) {
    // remove the last value from the stack
    const curIdx = stack.pop();
    // update value of current index/character to empty string
    res[curIdx] = "";
  }
  // convert array into string
  return res.join("");
};

console.log(minRemoveToMakeValid(string1));
