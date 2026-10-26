class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0

        for n in nums:
            # ignore the negative values
            if total < 0:
                total = 0
            # add n to the total
            total += n
            # keep track of max 
            res = max(res, total)
        
        return res 
       

# submission 2181761167 - 2026-10-25T22:11:11+00:00
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            
            if curr_sum < 0: 
                curr_sum = 0
            

        return max_sum