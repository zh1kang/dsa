class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        # We can implement kadane's but we have to modify it 
        # we keep track of curr_max, curr_min, and global_max
        # if we encounter a negative number we switch the max and mins to multiply 

        global_max = curr_max = curr_min = nums[0]

        for num in nums[1:]:
            # if we find a negative we flip to properly keep track of max
            if num < 0:
                curr_max, curr_min = curr_min, curr_max


            curr_max = max(curr_max, curr_max * num) 

        

# submission 2178011113 - 2026-10-21T14:11:06+00:00
class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        # We can implement kadane's but we have to modify it 
        # we keep track of curr_max, curr_min, and global_max
        # if we encounter a negative number we switch the max and mins to multiply 

        global_max = curr_max = curr_min = nums[0]

        for num in nums[1:]:
            # if we find a negative we flip to properly keep track of max
            if num < 0:
                curr_max, curr_min = curr_min, curr_max


            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            

            global_max = max(curr_max, global_max)

        return global_max  

        