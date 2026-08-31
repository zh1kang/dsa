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




        