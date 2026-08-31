class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        subset = []
        def backtrack(index):
            if len(subset) == k:
                res.append(subset[:])
                return

            for i in range(index, n + 1):
                subset.append(i)
                backtrack(i+1)
                subset.pop()

        backtrack(1)
        return res
            

        
        