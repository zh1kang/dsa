class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        

        res = set()
        visited = [False] * len(nums)                    
        

        def backtrack(path):
            if len(path) == len(nums):
                res.add(tuple(path))
                return

            for i, num in enumerate(nums):

                if visited[i]:
                    continue

                visited[i] = True
                path.append(num)
                backtrack(path)

                path.pop()
                visited[i] = False

        
        backtrack([])
        return [list(p) for p in res]

