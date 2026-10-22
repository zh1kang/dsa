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






        

# submission 2178149016 - 2026-10-21T16:45:48+00:00
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res = []

        def backtrack(idx, total, path):

            if total == target:
                res.append(path[:])

            elif total > target:
                return 

            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                remaining = total + candidates[i]
                backtrack(i, remaining, path)
                path.pop()

        backtrack(0, 0, [])
        return res 
                

            


        

# submission 2178150886 - 2026-10-21T16:47:40+00:00
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res = []

        def backtrack(idx, total, path):

            if total == target:
                res.append(path[:])
                return

            elif total > target or idx >= len(candidates):
                return 

            # option 1 we stay with the current number because of infinite reuse
            path.append(candidates[idx])
            backtrack(idx, total + candidates[idx], path)
            path.pop()

            # option 2 we skip
            backtrack(idx + 1, total, path)

        backtrack(0, 0, [])
        return res 
                

            


        