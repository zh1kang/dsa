class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(idx, path, total):
            # base case
            if total == target:
                res.append(path.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            
            # add the next number
            path.append(candidates[idx])
            backtrack(idx, path, total + candidates[idx])
            path.pop()
            
            # skip
            backtrack(idx + 1, path, total)

        backtrack(0, [], 0)
        return res 




        

# submission 2087595257 - 2026-07-30T14:11:19+00:00
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






        