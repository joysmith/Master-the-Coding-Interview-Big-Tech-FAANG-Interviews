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
  //  test case, if there is no head
  if (!head) return null;

  //  createing tortoise pointer from head
  let tortoise = head;
  //  createing hare pointer from head
  let hare = head;

  //  repeat until the hare and tortoise overlap/meet each other
  while (true) {
    //  move tortoise 1 step
    tortoise = tortoise.next;
    //  move hare 1 step
    hare = hare.next;

    // test case,for no cycle
    // if there is a single node or, node is pointing to tail
    if (hare === null || hare.next === null) {
      return null;
    } else {
      // move hare 1 more step, i.e 2 steps
      hare = hare.next;
    }

    // check, whenever tortoise and hare meet then, break this loop
    if (tortoise === hare) break;
  }

  // FINDING OUT LIST NODE WHERE CYCLE BEGIN
  // we know the tortoise and hare are at meeting point

  // create pointer1 from head
  let p1 = head;
  // create pointer2 from tortoise/hare
  let p2 = tortoise;

  // move p1 and p2, until they meet
  while (p1 !== p2) {
    // move p1 pointer
    p1 = p1.next;
    // move p2 pointer
    p2 = p2.next;
  }

  // return the node where the cycle begin/started
  return p2;
};

console.log(findCycle(linkedList));
