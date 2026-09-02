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
       