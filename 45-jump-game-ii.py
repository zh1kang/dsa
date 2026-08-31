class Solution:
    def jump(self, nums: List[int]) -> int: 
        start = end = jumps = 0 
        
        # end has to be less than the end index  
        while end < len(nums) - 1:
            # keep track of farthest jump 
            farthest = 0 

            for i in range(start, end + 1):
                farthest = max(farthest, i + nums[i])
            
            start = end + 1 
            end = farthest
            jumps += 1

        return jumps




    

        

        
        

# submission 1805637756 - 2025-10-19T05:39:45+00:00
class Solution:
    def jump(self, nums: List[int]) -> int: 
        curJumps = 0
        curReachable = 0
        nextReachable = 0
        for i in range (len(nums)-1):
            if i > curReachable:
                curJumps += 1
                curReachable = nextReachable
                nextReachable = 0
            nextReachable = max(nextReachable, i + nums[i])
        return curJumps





    

        

        
        

# submission 1805638518 - 2025-10-19T05:40:57+00:00
class Solution:
    def jump(self, nums: List[int]) -> int: 
        curJumps = 0
        curReachable = 0
        nextReachable = 0
        for i in range (len(nums)):
            if i > curReachable:
                curJumps += 1
                curReachable = nextReachable
                nextReachable = 0
            nextReachable = max(nextReachable, i + nums[i])
        
        return curJumps





    

        

        
        