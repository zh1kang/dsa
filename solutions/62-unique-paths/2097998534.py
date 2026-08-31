class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # looks like a DP problem, the robot can only move down or right
        # so there are two options that the robot can take at each time 
        
        # the state of this problem is dp(i, j) which are the possible steps the robot can take to get to the finish 
        
        # we can use memoization to store the previous paths
        memo = {} # O(1) initialization 
        def dfs(r, c): 
            # base case if they reach the end, O(1) comparisons
            if r == m - 1 or c == n-1:
                return 1
            if r >= m or c >= n:
                return 0

            # if the current row, column is already cached we just retrieve it
            if (r, c) in memo:
                return memo[(r,c)]      

            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1) # O(m*n)
            return memo[(r,c)]
        
        return dfs(0,0) #O(m*n) total
 
        