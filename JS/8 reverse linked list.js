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

var reverseList = function (head) {
  // initializing previous as null
  let prev = null;
  // get the current node we are working on
  let current = head;

  while (current) {
    // get the next node from the current node
    let nextTemp = current.next;
    // update the current node next to be with previous node
    current.next = prev;
    // store the list that we built so far
    prev = current;
    // move to next node that we stored
    current = nextTemp;
  }

  // return the linked list
  return prev;
};

printList(linkedList);
console.log("after reverse");
printList(reverseList(linkedList));
