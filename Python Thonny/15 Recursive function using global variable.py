# counter to count level
level = 0 

def inception():
    # always declare global variable at top
    global level
    # print current level
    print(level)

    # check base condition to stop function
    if (level > 3):
        return "done !"
    
    # increase level
    level += 1

    # calling recurcive function with return to bubble up value
    return inception()


print(inception())
# inception(inception(inception("done !")))