class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        res = []
        candidates.sort()

        def dfs(idx, path, total):
            if total == target:
                res.append(path.copy())
                return

            for i in range(idx, len(candidates)):
                # skip duplicates since we sorted, we can just check if the idx is different and if the candidates are the same
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if total + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()
            
        dfs(0, [], 0)
        return res
    
    

# submission 2133519745 - 2026-09-07T05:39:00+00:00
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        res = []
        candidates.sort()

        def dfs(idx, path, total):
            if total == target:
                res.append(path.copy())
                return

            for i in range(idx, len(candidates)):
                # skip duplicates since we sorted, we can just check if the idx is different and if the candidates are the same
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if total + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()
            
        dfs(0, [], 0)
        return res

        # TC: O(2^n) because of backtracking
        # SC: O(n)
    