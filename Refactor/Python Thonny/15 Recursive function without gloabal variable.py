# counter to count level
level = 0 

def inception(dream):
    # print current dream
    print(dream)

    # check base condition to stop dream/function
    if (dream > 3):
        return "done !"
    
    # increase dream
    dream += 1

    # calling recurcive function with return to bubble up value
    return inception(dream)


print(inception(level))
# inception(inception(inception("done !")))