class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res 

# submission 2086203410 - 2026-07-29T13:58:40+00:00
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        subset = []
        def backtrack(i):
            # base case if we reach the end of the array
            if i == len(nums):
                result.append(subset.copy())
                return

                
                
            # include the current
            subset.append(nums[i])
            backtrack(i+1)

            # exclude it
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return result




        

# submission 2086225228 - 2026-07-29T14:15:13+00:00
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        subset = []
        def backtrack(index):
            result.append(subset[:])

            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return result




        