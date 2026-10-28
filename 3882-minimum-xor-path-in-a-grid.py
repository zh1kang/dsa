class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        

        # we can use dynamic programming, we can use bottom up dp to track the minimum values for each previous xor 
        m = len(grid)
        n = len(grid[0])


        # this will store a set for all XOR sums to reach dp[i][j]
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    continue

                if j + 1 < n:
                    for val in dp[i][j]:
                        dp[i][j+1].add(val ^ grid[i][j + 1])

                if i + 1 < m:
                    for val in dp[i][j]:
                        dp[i+1][j].add(val ^ grid[i+1][j])

        
        return min(dp[m-1][n-1])

