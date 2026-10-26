class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # can we just take the bitwise AND of all values that are not in their position and return the max of this value
        
        curr_max = 0 
        for i in range(len(nums)):
            if nums[i] != i: 
                curr_max = max(curr_max, nums[i] & i)
            
        return curr_max

# submission 2179345538 - 2026-10-23T04:45:43+00:00
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # can we just take the bitwise AND of all values that are not in their position and return the max of this value
        if nums == sorted(nums):
            return 0 
       
        curr_max = 0 
        for i in range(len(nums)):
            if nums[i] != i: 
                curr_max = max(curr_max, nums[i] & i)
            
            
        return curr_max

# submission 2179346460 - 2026-10-23T04:47:12+00:00
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # can we just take the bitwise AND of all values that are not in their position and return the max of this value
        if nums == sorted(nums):
            return 0 
       
        ans = -1
        for i, num in enumerate(nums):
            if i != num:
                ans &= num

        return max(ans, 0)
