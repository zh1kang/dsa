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




        