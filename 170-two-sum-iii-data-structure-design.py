class TwoSum:

    def __init__(self):
        self.nums = []
        

    def add(self, number: int) -> None:
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        for i in range(len(self.nums)):
            target = value - self.nums[i]
        
            if target in self.nums:
                return True
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# submission 2157589354 - 2026-09-29T21:29:13+00:00
class TwoSum:

    def __init__(self):
        self.nums = []
        

    def add(self, number: int) -> None:
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        for i in range(len(self.nums)):
            target = value - self.nums[i]
        
            if target in self.nums:
                return True
        
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# submission 2157589937 - 2026-09-29T21:30:44+00:00
class TwoSum:

    def __init__(self):
        self.nums = []
        

    def add(self, number: int) -> None:
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        if len(self.nums) >= 2:
            for i in range(len(self.nums)):
                target = value - self.nums[i]
            
                if target in self.nums:
                    return True
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# submission 2157591000 - 2026-09-29T21:33:28+00:00
class TwoSum:

    def __init__(self):
        self.nums = {}
        

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        remaining = value - num
        for num in nums:
            if num != remaining:
                if remaining in self.nums:
                    return True
            elif self.nums[num] > 1:
                return True

        return False 
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# submission 2157591275 - 2026-09-29T21:34:09+00:00
class TwoSum:

    def __init__(self):
        self.nums = {}
        

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        
        for num in self.num.keys():
            remaining = value - num
            if num != remaining:
                if remaining in self.nums:
                    return True
            elif self.nums[num] > 1:
                return True

        return False 
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# submission 2157591332 - 2026-09-29T21:34:18+00:00
class TwoSum:

    def __init__(self):
        self.nums = {}
        

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        
        for num in self.nums.keys():
            remaining = value - num
            if num != remaining:
                if remaining in self.nums:
                    return True
            elif self.nums[num] > 1:
                return True

        return False 
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)