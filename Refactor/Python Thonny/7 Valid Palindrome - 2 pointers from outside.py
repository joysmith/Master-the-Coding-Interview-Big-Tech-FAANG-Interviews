import re

string = "A man, a plan, a canal: Panama"

def isValidPalindrome(s):
    # the regix pattern
    s = re.sub("[\W]", '', s).lower()
    
    # initialize left/right pointers at start and end of string respectively
    left = 0
    right =  len(s) -1
    
    # loop through string characters while comparing them, then move the pointers closer to the center
    while(left < right):
        # check, if left and right char are not same, then
        if(s[left] != s[right]):
            return False
        
        # move left pointer
        left += 1
        # move right pointer
        right -= 1
    
    
    return True


print(isValidPalindrome(string))
