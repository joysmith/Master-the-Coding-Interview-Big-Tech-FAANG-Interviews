'''
NOTE: The beginning portion builds our test case linked list. Scroll down to the section titled Our Solution for the code solution!
'''
from functools import reduce

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
  

# ---- Generate our linked list ----
# linkedList = [8,7,6,5,4,3,2,1].reduce((acc, val) => new ListNode(val, acc), null); --JS code
lis = [8,7,6,5,4,3,2,1]
linkedList = reduce(lambda acc, val: ListNode(val, acc), lis, None)

#    curr = linkedList, cycleNode = None
# TypeError: cannot unpack non-iterable NoneType object
# curr = linkedList, cycleNode = None
# https://www.youtube.com/watch?v=hRASFmdKRdw

curr = linkedList
cycleNode = None

while(curr.next != None):
    if(curr.val == 3):
        cycleNode = curr
  
    curr = curr.next


curr.next = cycleNode
# ---- Generate our linked list ----

# --------- Our solution -----------

def findCycle(head):

    # test case, if there is no head
    if(not head):
        return None
    
    # createing tortoise pointer from head
    tortoise = head
    # createing hare pointer from head
    hare = head
  
    # repeat until the hare and tortoise overlap/meet each other
    while(True):
        # move tortoise 1 step
        tortoise = tortoise.next
        # move hare 1 step
        hare = hare.next
    
        # test case,for no cycle
        # if there is a single node
        # or, node is pointing to tail 
        if(hare == None or hare.next == None):
            return None
        else:
            # move hare 1 more step, i.e 2 steps
            hare = hare.next
        
        # check, whenever tortoise and hare meet then,
        if(tortoise == hare):
            # break this loop
            break
    

    # FINDING OUT LIST NODE WHERE CYCLE BEGIN   
    # we know the tortoise and hare are at meeting point
    # create pointer1 from head 
    p1 = head
    # create pointer2 from tortoise/hare
    p2 = tortoise
  
    # move p1 and p2, until they meet
    while(p1 != p2):
        # move p1 pointer
        p1 = p1.next
        # move p2 pointer
        p2 = p2.next
    
    # return the node where the cycle begin/started
    return p2


print(findCycle(linkedList))

# extra
cyclePoint = findCycle(linkedList)
print(cyclePoint.val)