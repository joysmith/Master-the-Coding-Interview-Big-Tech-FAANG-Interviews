def validPalindrome(s):
    start = 0
    end = len(s) - 1
    while (start < end):

        if (s[start] != s[end]):
            return validSubPalindrome(s, start + 1, end) or validSubPalindrome(s, start, end - 1)
      
        start += 1
        end -= 1
  
    return True


def validSubPalindrome(s, start, end):

    while (start < end):
        if (s[start] != s[end]):
            return False
      
    start += 1
    end -= 1
  
    return True
