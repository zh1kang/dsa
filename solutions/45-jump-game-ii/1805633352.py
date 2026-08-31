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




    

        

        
        