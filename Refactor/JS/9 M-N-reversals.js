/*
NOTE: The beginning portion builds our test case linked list. Scroll down to the section titled Our Solution for the code solution!
 */
// template to create list node
class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}
// ---- Generate our linked list ----
const linkedList = [5, 4, 3, 2, 1].reduce(
  (acc, val) => new ListNode(val, acc),
  null
);

// ---- Print our linked list ----

const printList = (head) => {
  if (!head) {
    return;
  }

  console.log(head.val);
  printList(head.next);
};

// --------- Our solution -----------

var reverseBetween = function (head, m, n) {
  // initialize current node position to 1
  let currentPos = 1,
    // node we are working on
    currentNode = head;
  // m-1 node
  let start = head;

  // get m-1 position
  while (currentPos < m) {
    // capture m-1 node during iteration
    start = currentNode;
    // move to next node
    currentNode = currentNode.next;
    // increment position
    currentPos++;
  }

  // the list so far
  let newList = null,
    // the node that will end up as an tail
    tail = currentNode;

  // iterate through our reversal steps within m & n
  while (currentPos >= m && currentPos <= n) {
    // store next node
    const next = currentNode.next;
    //  update current node property
    currentNode.next = newList;
    // update list so far
    newList = currentNode;
    // update current node to next node that we stored before
    currentNode = next;
    // move position
    currentPos++;
  }

  // assembling the linked list segments
  // assemble m node
  start.next = newList;
  // assemble n+1 node
  tail.next = currentNode;

  if (m > 1) {
    return head;
  } else {
    return newList;
  }
};

printList(linkedList);
console.log("after reverse");
printList(reverseBetween(linkedList, 2, 4));

//  1
//  2
//  3
//  4
//  5
//  after reverse
//  1
//  4
//  3
//  2
//  5
