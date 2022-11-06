
#NOTE: The beginning portion builds our test case linked list. Scroll down to the section titled Our Solution for the code solution!
from functools import reduce

class ListNode:
    def __init__(self, val, next = None):
            self.val = val
            self.next = next


# ---- Generate our linked list ----
# const linkedList = [5, 4, 3, 2, 1].reduce((acc, val) => new ListNode(val, acc), null); JS-code

lis = [5, 4, 3, 2, 1]
linkedList = reduce(lambda acc, val: ListNode(val, acc), lis, None)

# ---- Generate our linked list ----

def printList(head):
    if(not head):
        return
  
    print(head.val)
    printList(head.next)

# --------- Our solution -----------

def reverseBetween(head, m, n):
    # initialize current node position to 1
    currentPos = 1 
    # node we are working on
    currentNode = head
    # m-1 node
    start = head
  
    # get m-1 position
    while(currentPos < m):
        # capture m-1 node during iteration
        start = currentNode
        # move to next node
        currentNode = currentNode.next
        # increment position
        currentPos += 1
  
    # the list so far
    newList = None 
    # the node that will end up as an tail 
    tail = currentNode
  
    # iterate through our reversal steps within m & n
    while(currentPos >= m and currentPos <= n):
        # store next node
        next = currentNode.next
        # update current node property 
        currentNode.next = newList
        # update list so far
        newList = currentNode
        # update current node to next node that we stored before
        currentNode = next
        # move position
        currentPos += 1
  
    # assembling the linked list segments
    # assemble m node
    start.next = newList
    # assemble n+1 node
    tail.next = currentNode
  
    # 
    if(m > 1):
        return head
    else:
        return newList
  

printList(linkedList)
print('after reverse')
printList(reverseBetween(linkedList, 2, 4))




#   1
#   2
#   3
#   4
#   5
#   after reverse
#   1
#   4
#   3
#   2
#   5
