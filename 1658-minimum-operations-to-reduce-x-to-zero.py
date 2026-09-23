class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        total = sum(nums)
        # the target is how many values we can keep
        target = total - x 

        if target < 0: 
            return -1

        if target == 0:
            return len(nums)

        l = 0 
        curr = 0
        max_len = -1

        for r in range(len(nums)):
            curr += nums[r]

            while curr > target:
                curr -= nums[l]
                l += 1
            if curr == target:  
                max_len = max(max_len, r - l + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len

            



        
        