class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        # we can use dp and store our choices in memo 
        memo = {}
        rows, cols = len(grid), len(grid[0])
        def dp(i,j):
            curr_sum = 0
            # base case we reached the end 
            if i == rows - 1 and j == cols - 1:
                return grid[i][j]
            # if out of bounds 
            if i >= rows or j >= cols:
                return float('inf')

            if (i,j) in memo:
                return memo[(i,j)]
           
            memo[(i,j)] = grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))
            return memo[(i,j)]

        return dp(0,0)
        

# submission 2151329083 - 2026-09-23T19:49:47+00:00
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # bottom-up dp 

        rows, cols = len(grid), len(grid[0])

        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                # reached the end
                if i == rows - 1 and j == cols - 1:
                    dp[i][j] = grid[i][j]

                # we can't move more right so can only move down
                elif i == rows - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                # can't move more down so we have to move right
                elif j == cols - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]

                # if it is none of these cases we just take the min of the next move
                else: 
                    dp[i][j] = grid[i][j] + min(
                        dp[i+1][j],
                        dp[i][j + 1])

        return dp[0][0]

        
        

# submission 2151330365 - 2026-09-23T19:51:47+00:00
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # bottom-up dp 

        rows, cols = len(grid), len(grid[0])

        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                # reached the end
                if i == rows - 1 and j == cols - 1:
                    dp[i][j] = grid[i][j]

                # we can't move more right so can only move down
                elif i == rows - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                # can't move more down so we have to move right
                elif j == cols - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]

                # if it is none of these cases we just take the min of the next move
                else: 
                    dp[i][j] = grid[i][j] + min(
                        dp[i+1][j],
                        dp[i][j + 1])

        return dp[0][0]

        # TC: O(mn) because we iterate through rows and cols
        # SC: O(mn) we store a value for every cell  

        
        