# test case 1
#string = "{([])}"

# test case 2
# string = "{([)]}"

# test case 3
# string = "{()[]}"

# test case 4
# string = ""

# test case 5
string = "{([]"


# create hash table data model 
parens = {
    '(': ')',
    '{' : '}',
    '[': ']'
}

def isValid(s):
    # test case: Is input is empty string
    if(len(s) == 0): return True
    
    # initialize stack data model using array
    stack = []
  
  # for loop to iterate our string
    for i in range(len(s)):
        # Is left bracket is stored in Hash table data model
        if(parens.get(s[i])):
            # store, left bracket in stack data model
            stack.append(s[i])
        else:
            # remove, left bracket from stack data model, and get it 
            leftBracket = stack.pop()
            # retrive, value of leftBracket from hash table data model, and get it
            correctBracket = parens[leftBracket]

            # now compare does sting char/bracket index is not equal to left bracket  
            if(s[i] != correctBracket):
                return False
        
     
    # Is stack is empty
    return len(stack) == 0


print(isValid(string))
