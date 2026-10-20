class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        # stack is lifo so the value we append should go to the back 
        # this for loop rotates all the values in the current queue
        # to the right to simulate LIFO
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# submission 2175812567 - 2026-10-19T01:47:05+00:00
class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        # stack is lifo so the value we append should go to the back 
        # this for loop rotates all the values in the current queue
        # to the right to simulate LIFO
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()