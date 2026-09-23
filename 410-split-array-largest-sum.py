class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        def feasible(max_sum: int):
            subarray = 1
            curr_sum = 0 
            
            for num in nums:
                if curr_sum + num > max_sum:
                    curr_sum = num 
                    subarray += 1

                else:
                    curr_sum += num 
            return subarray <= k


        left, right = max(nums), sum(nums)
        ans = right

        while left <= right: 
            mid = (left + right) // 2

            if feasible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans           