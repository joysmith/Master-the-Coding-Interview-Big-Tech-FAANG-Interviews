import re

string = "A man, a plan, a canal: Panama"

def isValidPalindrome(s):
    # https://www.youtube.com/watch?v=9RksQ5YT7FM
    # s = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase()  --JS code
    # the regix pattern
    s = re.sub("[\W]", '', s).lower()
    print(s)

    # to store reverse string data model
    rev = ""
 

    # generate a reverse string using a reverse for loop.
    # Python range(start, stop, step)
    for i in range(len(s) -1, -1, -1):
        #(let i = s.length - 1; i >= 0; i--) {   --JS code
        rev += s[i]
    
    # check, are both string same or not
    return rev == s

print(isValidPalindrome(string))
