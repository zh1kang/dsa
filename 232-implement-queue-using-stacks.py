class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()     

        

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self) -> bool:
        return not self.output and not self.input
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# submission 2128509852 - 2026-09-02T14:02:38+00:00
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()     

        

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self) -> bool:
        return not self.output and not self.input
        
# divergences:
# none
# stacks are LIFO and queues are FIFO so appending all items in one stack to another reverses this and gives us the proper behavior we want for a queue 

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# submission 2134051479 - 2026-09-07T15:25:12+00:00
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
       

        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        # we want to pop the top, but since stacks are LIFO, we reverse it by appending everything in input to ouput 
        
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output.pop()
        
        

    def peek(self) -> int:

        # peek checks the element in the front of the queue; so we do the same thing and return self.output[-1]

        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]
       

    def empty(self) -> bool:
        return not self.input and not self.output
        
# divergences:
# none
# stacks are LIFO and queues are FIFO so appending all items in one stack to another reverses this and gives us the proper behavior we want for a queue 

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()