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





    

        

        
        