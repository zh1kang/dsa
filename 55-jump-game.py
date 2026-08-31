class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= goal:
                goal = i 

        return True if goal == 0 else False 



# submission 1805619508 - 2025-10-19T05:10:47+00:00
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= goal:
                goal = i 

        return True if goal == 0 else False 


