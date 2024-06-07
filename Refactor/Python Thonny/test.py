string = "abcdgfgfg"

seen = {}
left = 0 
longest = 0

for left in range(len(string)):
  currentChar = string[left]

  seen[currentChar] = left
  
  previouslySeenChar = seen[currentChar]




print(previouslySeenChar)



















































# seen = {}
# string = "au"

# seen[string]

# print(seen)


# my_list = ['Nagendra','Babu','Nitesh','Sathya']
# my_dict = dict() 
# for index,value in enumerate(my_list):
#   my_dict[value] = index
# print(my_dict)
# #OUTPUT
# {0: 'Nagendra', 1: 'Babu', 2: 'Nitesh', 3: 'Sathya'}