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