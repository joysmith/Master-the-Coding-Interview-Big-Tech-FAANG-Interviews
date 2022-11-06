# Array in javascript are just obj with integer based Keys, that act like index

class MyArray:
    def __init__(self):
        # lenght/key counter 
        self.length = 0
        # data model to store strings
        self.data = {}

    # 
    def get(self, index):
        return self.data[index]
    
    
    def push(self, item):
        # add item to dict data model 
        self.data[self.length] = item
        # increase key/length
        self.length += 1
        # return dict data model if they wanna print()
        return self.data
    
    def pop(self):
        # 
        lastItem = self.data[self.length - 1]
        # delete last item from dict data model using key
        del self.data[self.length - 1]
        # decrement key/length value
        self.length -= 1
        # return last item, if they wanna print()
        return lastItem
    
    def deleteAtIndex(self, index):
        # get the item by key 
        item = self.data[index]
        # perform shifting operation
        self.shiftItems(index)
        # return item, if they wanna print()
        return item
    
    def shiftItems(self, index):
        #for (let i = index; i < self.length - 1; i++) { --JS code
        for i in range(index, self.length -1):
            self.data[i] = self.data[i + 1]
        
        print(self.data[self.length - 1])
        # delete last item to declutter
        del self.data[self.length - 1]
        # decrement lenght/key value 
        self.length -= 1
    


myArray =  MyArray()
print(myArray.push('hi'))
print(myArray.push('you'))
print(myArray.push('are'))
print(myArray.push('smart'))
print(myArray.push('!'))
print("remove: " + myArray.pop())


print(myArray.deleteAtIndex(0))
myArray.shiftItems(0)

print(myArray.data)

