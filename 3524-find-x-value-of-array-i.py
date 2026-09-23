class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        
        res = [0] * k
        for left in range(len(nums)):
            product = 1
            for right in range(left, len(nums)):
                product *= nums[right]

                remainder = product % k

                res[remainder] += 1

        return res

# submission 2149156440 - 2026-09-21T23:26:05+00:00
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        
        # thoughts:
        # removing a prefix and suffix is the same as choosing any nonempty contiguous subarray
        # so fore every contiguous subarray we compute its product % k and count how many subarrays give each remainder 0 ... k - 1

        res = [0] * k

        # dp[r] = number of subarrays ending at the previous index which has product % k == r

        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            rem = num % k

            # case 1: start new subarray
            new_dp[rem] += 1

            # case 2: extend every subarray ending at prev index
            for r in range(k):
                new_r = (r * rem) % k
                new_dp[new_r] += dp[r]

            # every subarray representid in new dp is valid reaminder
            for r in range(k):
                res[r] += new_dp[r]

            dp = new_dp

        return res




