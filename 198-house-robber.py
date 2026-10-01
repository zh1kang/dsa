class Solution:
    def rob(self, nums: list[int]) -> int:
        
        memo = {}

        def dp(i):

            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            # option 1 we skip
            skip = dp(i + 1)

            # option 2
            rob = nums[i] + dp(i+2)

            memo[i] = max(skip, rob)
            return memo[i]

        return dp(0)

        # TC: O(n)
        # SC: O(1)


# submission 2156456350 - 2026-09-28T21:05:16+00:00
class Solution:
    def rob(self, nums: list[int]) -> int:
        
        memo = {}

        def dp(i):

            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            # option 1 we skip
            skip = dp(i + 1)

            # option 2
            rob = nums[i] + dp(i+2)

            memo[i] = max(skip, rob)
            return memo[i]

        return dp(0)

        # TC: O(n)
        # SC: O(n)

