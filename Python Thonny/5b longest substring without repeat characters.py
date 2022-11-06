string = "ausdsd"

def lengthOfLongestSubstring(s):
    if(len(s) <= 1):
      return len(s)
    
    seen = {}
    left = 0 
    longest = 0
    
    for right in range(len(s)):
        currentChar = s[right]
        seen[currentChar] = right
        # print(seen)
        previouslySeenChar = seen[currentChar]

        if(previouslySeenChar >= left):
          left = previouslySeenChar + 1
              
        seen[currentChar] = right
        
        longest = max(longest, right - left + 1)
    
    return longest

print(lengthOfLongestSubstring(string))
