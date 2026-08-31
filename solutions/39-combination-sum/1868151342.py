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




        