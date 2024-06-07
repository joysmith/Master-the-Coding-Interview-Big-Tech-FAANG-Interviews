
#NOTE: The beginning portion builds our test case linked list. Scroll down to the section titled Our Solution for the code solution!

class ListNode:
    def __init__(self, val, prev = None, next = None, child = None):
            self.val = val
            self.next = next
            self.prev = prev
            self.child = child

# ---- Generate our linked list ----
nodes = [1, [2, 7, [8, 10, 11], 9], 3, 4, [5, 12, 13], 6]

def buildMultiLevel(nodes):
    head = ListNode(nodes[0])
    currentNode = head

    #start from 1 
    for i in range(1, len(nodes)):
        val = nodes[i]
        nextNode = None

        if isinstance(val, list):
        # if(Array.isArray(val)): -JS code
            nextNode = buildMultiLevel(val)
            currentNode.child = nextNode
            continue
    

        nextNode = ListNode(val)
        currentNode.next = nextNode
        nextNode.prev = currentNode
        currentNode = nextNode
  
  
    return head


multiLinkedList = buildMultiLevel(nodes)

# ---- Generate our linked list ----

def printListMulti(head):

    if(not head):
        return
  

    print(head.val)

    if(head.child):
        printListMulti(head.child)
  

    printListMulti(head.next)


def printList(head):
    if(not head):
        return
  

    print(head.val)
  
    printList(head.next)


# --------- Our solution -----------

def flatten(head):
    # test case, if there is no node aka null then
    if (not head):
        return head

    # get the working node
    currentNode = head

    # check, if current node does not equal to null
    while (currentNode != None):

        # check, if current node doesn't have child then,
        if (currentNode.child == None):
            # move current node to next node
            currentNode = currentNode.next
        else:# default there is a child in node then,

            tail = currentNode.child

            # 
            while (tail.next != None):
                tail = tail.next
       

            tail.next = currentNode.next
            if (tail.next != None):
                tail.next.prev = tail
          

            currentNode.next = currentNode.child
            currentNode.next.prev = currentNode
            currentNode.child = None
    
    return head


printListMulti(multiLinkedList)
print('after flatten')
printList(flatten(multiLinkedList))



#  1
#  2
#  7
#  8
#  10
#  11
#  9
#  3
#  4
#  5
#  12
#  13
#  6
# after flatten
#  1
#  2
#  7
#  8
#  10
#  11
#  9
#  3
#  4
#  5
#  12
#  13
#  6