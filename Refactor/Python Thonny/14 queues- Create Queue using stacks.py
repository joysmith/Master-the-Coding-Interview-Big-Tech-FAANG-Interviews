class QueueWithStacks:
    def __init__(self):
        #initialize stack1 from enqueue/push value
        self.input = []
        #initialize stack2 from dequeu/pop value
        self.out = []

        #append a value to the end of the queue
        def enqueue(val):
            self.input.push(val)
  
        #remove and the value at the start of the queue
        def dequeue():
            #if stack2 is empty
            if (self.out.length == 0):
                #if there is a length inside stack1
                while(self.input.length > 0):
                    #pop value from stact1 then append value to stack2
                    self.out.append(self.input.pop())
      
            return self.out.pop()
  

        #return the value at the start of the queue
        def peek():
            if (self.out.length == 0):
                while(self.input.length > 0):
                    self.out.push(self.input.pop())
        
            # return the last value of array
            return self.out[self.out.length - 1]
  

        #check is queue is empty or not
        def empty():
            return self.input.length == 0 and self.out.length == 0


  
