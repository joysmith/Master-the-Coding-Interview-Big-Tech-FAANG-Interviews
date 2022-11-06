import re
import math
string = "A man, a plan, a canal: Panama"

def isValidPalindrome(s):
    # regix pattern
    s = re.sub("[\W]", '', s).lower()

    
    # initialize left/right pointers to point at the middle index of the string.
    # Remember, indexes start at 0 meaning that we have to floor() the value from dividing length by 2 in order to get the index of the center.
    left = math.floor(len(s) / 2)
    right = left
    
    # if the string is even, move left pointer back by 1 so left/right are pointing at the 2 middle values respectively.
    if(len(s) % 2 == 0):
        left -= 1
    
    
    # loop through the string while expanding pointers outwards comparing the characters.
    while(left >= 0 and right < len(s)):
        # check, if left and right char are not same, then
        if(s[left] != s[right]):

            return False
        
        # move left pointer
        left -= 1
        #move right pointer
        right +=1 
    
    
    return True


print(isValidPalindrome(string))
