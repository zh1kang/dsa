class Logger:

    def __init__(self):
        self.seen = defaultdict(list)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message in self.seen and timestamp < self.seen[message]:
            return False

        self.seen[message] = timestamp + 10

        return True 


             

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)