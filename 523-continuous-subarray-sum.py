class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        # we would continuously build a prefix sum and continously check modulo k, if we've seen it before there is an existing contiguous subarray that satisfies what we want

        prefix = 0
        seen = {0:-1}

        for i, num in enumerate(nums):
            prefix += num
            rem = prefix % k
            # if we've seen the remainder already
            if rem in seen:
                if i - seen[rem] >= 2:
                    return True

            else:
                seen[rem] = i

        return False  

        