class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        numIslands = 0
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(i, j):
            if (i >= row or j >= col or grid[i][j] == "0"):
                return 

            grid[i][j] = "0" # sink our current island to keep track 
            for di, dj in dir:
                dfs(i + di, j + dj)
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    numIslands += 1
        return numIslands


    