#string = "abcdcabb"
string = "abccabb"

#  Time: O(N^2);
#  Space: O(N)

def lengthOfLongestSubstring(s):
    #test case, if string length is 0 or 1
    if(len(s) <= 1):
        return len(s)
    
    # string length counter
    longest = 0
    
    # how to create a left pointer
    for left in range(len(s)):
        # create a dict data model to strore the character we have seen
        seenChars = {}
        # where to store the length of substring
        currentLength = 0

    # how to create a right pointer
        for right in range(left ,len(s)):
            # get the current character from string data model
            currentChar = s[right]
            
            #check do the current char exist in dictioary if not do this    
            if (not currentChar in seenChars):
                # increate substring length by 1
                currentLength += 1
                # store the current char in seen dict. 
                seenChars[currentChar] = True
                # compare the length of previous string with new string
                longest = max(longest, currentLength)
            else:# default if char exist in seen dict then
                # break this right pointer for loop
                break
           
    return longest


print(lengthOfLongestSubstring(string))
