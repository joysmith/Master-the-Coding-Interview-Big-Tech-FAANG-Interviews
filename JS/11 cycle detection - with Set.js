/*
NOTE: The beginning portion builds our test case linked list. Scroll down to the section titled Our Solution for the code solution!
 */

class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

// ---- Generate our linked list ----
const linkedList = [8, 7, 6, 5, 4, 3, 2, 1].reduce(
  (acc, val) => new ListNode(val, acc),
  null
);

let curr = linkedList,
  cycleNode;
while (curr.next !== null) {
  if (curr.val === 3) {
    cycleNode = curr;
  }

  curr = curr.next;
}

curr.next = cycleNode;
// ---- Generate our linked list ----

// --------- Our solution -----------
const findCycle = function (head) {
  // set datamodel to store the node we visited
  const seenNodes = new Set();
  //get the working node
  let currentNode = head;
  // check, Does this current node, doesnt exist in Set data model then,

  while (!seenNodes.has(currentNode)) {
    // test case, when there is no cycle
    if (currentNode.next === null) {
      return false;
    }
    // add current node to seen node Data model
    seenNodes.add(currentNode);
    // move current node to next node
    currentNode = currentNode.next;
  }
  // return node where cycle begins at
  return currentNode;
};

console.log(findCycle(linkedList.val));
