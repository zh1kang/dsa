class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        # convert all the zeros into -1's
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1 
        
        sum_idx = {0:-1}
        curr_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            curr_sum += num

            if curr_sum in sum_idx:
                max_len = max(max_len, i - sum_idx[curr_sum])

            else:
                sum_idx[curr_sum] = i

        return max_len 



    