string1 = "ab#z"
string2 = "az#z"


# function to create string data model without #-tag
def buildString(string):
    # create a list data model
    builtString = []

    # how to create a p pointer for traversal in string data model
    for p in range(len(string)):

        # check, element is not #, then
        if string[p] != '#':
            # add this element to our list data model
            builtString.append(string[p])
        else: # default case, element is equal to #, then
            # remove the last element from our list data model
            builtString.pop()       
    
    return builtString


# function to compare string data model
def backspaceCompare(S, T):
    # get string without #-tag
    finalS = buildString(S)
    # get string without #-tag
    finalT = buildString(T)
    

    # check, if length of two string data model are not equal, then
    if(len(finalS) != len(finalT)):
        return False 
    else:# default, if length of two string data model are equal, then

        # create p pointer
        for p in range(len(finalS)):
            
            # check, if elements in both string data model are not equal
            if(finalS[p] != finalT[p]):
                return False 
                        
    return True 

print(backspaceCompare(string1, string2))
     