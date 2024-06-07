'''
NOTE: The beginning portion builds our test case linked list.
Scroll down to the section titled Our Solution for the code solution!
'''

from functools import reduce

# template to create node list
class ListNode:
    def __init__(self, val, next = None):
            self.val = val
            self.next = next

# ---- Generate our linked list ----
#linkedList = [5, 4, 3, 2, 1].reduce((acc, val) => new ListNode(val, acc), null) JS-code
# linkedList = reduce(lambda acc, val: ListNode(val, acc), [5, 4, 3, 2, 1], None) # one line code
# https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
lis = [5, 4, 3, 2, 1]
linkedList = reduce(lambda acc, val: ListNode(val, acc), lis, None)



# ---- Print our linked list ----

def printList(head):
    if(not head):
        return

    print(head.val)
    printList(head.next)


# --------- Our solution -----------

def reverseList(head):
    # initializing previous as None
    prev = None
    # get the current node we are working on
    current = head
  
    while(current):
        # get the next node from the current node
        nextTemp = current.next
        # update the current node next to be with previous node
        current.next = prev
        # store the list that we built so far
        prev = current
        # move to next node that we stored
        current = nextTemp
    # return the linked list
    return prev


printList(linkedList)
print('after reverse')
printList(reverseList(linkedList))
