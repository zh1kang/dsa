class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        combinations = []

        def backtrack(index, total):
            if total == target:
                res.append(combinations[:])
            if total > target:
                return
            
            for i in range(index, len(candidates)):
                combinations.append(candidates[i])
                remaining = total + candidates[i]
                backtrack(i, remaining)
                combinations.pop()

        backtrack(0, 0)
        return res 






        