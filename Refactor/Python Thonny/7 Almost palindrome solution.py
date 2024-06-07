string = "poop"


def validPalindrome(s):
    # create left pointer
    start = 0
    # create right pointer
    end = len(s) - 1
    #run the pointer until they meet/overlap each other
    while (start < end):
        # check, start and end, char are not same then,
        if (s[start] != s[end]):
            #skip one char from left
            return (validSubPalindrome(s, start + 1, end)
            # skip one char from right
             or validSubPalindrome(s, start, end - 1))

        # move left pointer
        start += 1
        # move right pointer
        end -= 1
  
    return True

# fuction to check the string is valid palindrom
def validSubPalindrome(s, start, end):
    # move left and right pointer until they meet eachother
    while (start < end):
        #check, left and right poiter char are not same, then
        if (s[start] != s[end]): 
            return False
      
        # move left pointer
        start += 1
        # move right pointer
        end -= 1
     
    return True


print(validPalindrome(string))