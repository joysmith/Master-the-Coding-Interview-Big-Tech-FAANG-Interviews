string1 = "ab#z"
string2 = "az#z"


def backspaceCompare(S, T):
    p1 = len(S) - 1
    p2 = len(T) - 1

    while(p1 >= 0 or p2 >= 0):
        if(S[p1] == "#" or T[p2] == "#"):
            if(S[p1] == "#"):
                backCount = 2               
                while(backCount > 0):
                    p1 -= 1
                    backCount -= 1
                    
                    if(S[p1] == "#"):
                        backCount += 2                                   
            
            if(T[p2] == "#"):
                backCount = 2            
                while(backCount > 0):
                    p2 -= 1
                    backCount -= 1
                    
                    if(T[p2] == "#"):
                        backCount += 2                                                
        else:
            if(S[p1] != T[p2]):
                return False
            else:
                p1 -= 1
                p2 -= 1
                
    return True

print(backspaceCompare(string1, string2))