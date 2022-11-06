
# NOTE: The beginning portion builds our test case linked list. Scroll down to the section titled Our Solution for the code solution!
from functools import reduce

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
# ---- Generate our linked list ----
# const linkedList = [8,7,6,5,4,3,2,1].reduce((acc, val) => new ListNode(val, acc), null); --JS code

lis = [8,7,6,5,4,3,2,1]
linkedList = reduce(lambda acc, val: ListNode(val, acc), lis, None)


# https://www.youtube.com/watch?v=hRASFmdKRdw
#curr = linkedList, cycleNode = None
#TypeError: cannot unpack non-iterable NoneType object
#curr = linkedList, cycleNode = None
curr = linkedList
cycleNode = None


while(curr.next != None):
    if(curr.val == 3):

        cycleNode = curr
  
    curr = curr.next


curr.next = cycleNode
# ---- Generate our linked list ----

#  --------- Our solution -----------
def findCycle(head):
    # set datamodel to store the node we visited
    # seenNodes =  Set()  --JS code
    seenNodes =  set()
    # get the working node
    currentNode = head
  
    #   while(!seenNodes.has(currentNode)) {  -JS code with Set() Data model
    # https://appdividend.com/2022/06/01/python-set-contains/#:~:text=a%20single%20variable.-,Python%20set%20contains,%2C%20string%2C%20set%2C%20etc.
    # check, Does this current node, doesnt exist in Set data model then,
    while(not currentNode in seenNodes):

        # test case, when there is no cycle
        if(currentNode.next == None):
            return False

        # add current node to seen node Data model
        seenNodes.add(currentNode)

        # move current node to next node
        currentNode = currentNode.next
  
    # return node where cycle begins at
    return currentNode


print(findCycle(linkedList))

# extra
cycleAt =findCycle(linkedList)
print(cycleAt.val)