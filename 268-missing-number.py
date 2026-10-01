class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        seen = set()

        for num in nums:
            seen.add(num)

        for i in range(len(nums) + 1):
            if i not in seen:
                return i

        return -1


        

# submission 2158671385 - 2026-10-01T01:05:12+00:00
class Solution:
    def missingNumber(self, nums: list[int]) -> int:


        num_set = set()

        # add to set
        for num in nums:
            if num not in num_set:
                num_set.add(num)

        # iterate through

        for i in range(len(nums) + 1):
            if i not in num_set:
                return i



        