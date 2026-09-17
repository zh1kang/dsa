class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # so having the same end points is allowed 
        # we cannot have it within the interval though
        # so we have to have some sort of condition where if say R1 > L2? 
        # num of ways so this is some sort of dp problem
        MOD = 10**9 + 7 
        memo = {} 
        def dfs(idx, remaining):
            # base case, we made a successful segment
            if remaining == 0:
                return 1 
            
            # if we ran out of points but still need segments
            if idx >= n - 1:
                return 0 
            # cache
            if (idx, remaining) in memo:
                return memo[(idx, remaining)]
            total = 0 

            # choice 1: dont start at idx 
            total += dfs(idx + 1, remaining)
            
            # choice 2: start at the idx
            for end in range(idx+1, n):
                total += dfs(end, remaining - 1)

            memo[(idx, remaining)] = total % MOD
            
            return memo[(idx, remaining)]

        return dfs(0, k)

        # TC: idx * remaining = O(nk), 
        # looping over end = O(n)
        # total = O(n^2k)

        # SC: at worst case we are just storing all idx and remaining so O(nk)


        
