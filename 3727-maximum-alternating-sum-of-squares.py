class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # to maximize the alternating sum we want it so that everytime we subtract a value, the number is as small as possible 
        # sign doesn't matter here since it is a sum of squares 
        # for even indicies we take the largest number
        # for odd indicies we take the smallest number
    
        # can we sort the nums by abs value and then for the right pointer we take it, and then increment and then for left pointer we take the smallest and increment

        pos_nums = [abs(x) for x in nums]

        pos_nums.sort()

        l, r = 0, len(pos_nums) - 1 
        count = 0 
        score = 0
        while l <= r:
            # even so we take the right
            if count % 2 == 0:
                score += pos_nums[r] ** 2
                count += 1
                r -= 1
            elif count % 2 != 0:
                score -= pos_nums[l] ** 2
                count += 1
                l += 1

        return score 



            

        