class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(idx, subset):
            if idx == len(nums):
                res.append(subset[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()
        
        
        backtrack(0, [])
        return res 


        

# submission 2142026779 - 2026-09-14T22:08:38+00:00
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(idx, subset):
            res.append(subset[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
               
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        
        backtrack(0, [])
        return res 


        