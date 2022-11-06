
# NOTE: The beginning portion builds our test case binary tree. Scroll down to the section titled Our Solution for the code solution!

# ------- Code to generate our binary tree -------
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    # PUT A note HERE------------------------------------------------------------------------------------->
    def __getitem__(self, key):
        return self.__dict__[key]
  
      
    # note:python using self to remove "type error" in class definition
    # TypeError: TreeNode.insert() takes 1 positional argument but 2 were given
    def insert(self, values):
    # insert(values) {  JS-code

        #get the  node
        queue = [self]
        i = 0
        while (len(queue) > 0):
            # get the current node
            current = queue.pop(0)
            # let current = queue.shift(); JS-code


            for side in ["left", "right"]:
            # for (let side of ["left", "right"]) { JS-code
 
                # prob sol ------------------------------------------------------------------------------------>
                # check, if current node has no links to L & R nodes
                if (not current[side]):
                    # check, in value list the value is not None 
                    if (values[i] != None):
                        # check, node side is left then
                        if(side == "left"):
                            # create a new node and add link of this new node, to current node left side
                            current.left =  TreeNode(values[i])
                        else: # default, node side is right then
                            # create a new node and add link of this new node, to current node right side
                            current.right =  TreeNode(values[i])
                    
                    # increase counter    
                    i += 1

                    #check, counter i value is bigger than, values list array then,
                    if (i >= len(values)):
                            # return root node
                            return self

                if (current[side]):
                    queue.append(current[side])
      
    
        return self
  

# create root node 
root = TreeNode()

# create other node and link them like a binary tree structure
root.insert([1, 1, 1, 1, None, None, None, 1, None, None, None, 1, None, None])
'''
l r     l r     l r     l r     l r     l r     l r 
1 1     1 1     N N     N 1     N N     N 1     N N

                              root
                      /                 \
                    1                       1
                /       \               /      \
            1               1       None        None
        /       \          /  \
    None        1      None    None 
            /      \
        None        1 
                /       \
            None        None
'''


# ------- Code to generate our binary tree -------

# ------- Our Solution -------
def maxDepth(node, currentDepth):
    # base condition
    if (not node):
        return currentDepth
    
    # increate level depth by 1
    currentDepth += 1
    
    # base condition 2, call recursive function 
    return max(maxDepth(node.right, currentDepth), maxDepth(node.left, currentDepth))

print(maxDepth(root, 0))