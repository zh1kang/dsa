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


    

# submission 1833901003 - 2025-11-19T05:36:51+00:00
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        numIslands = 0
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(i, j):
            if (i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == "0"):
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


    

# submission 2089517313 - 2026-08-01T05:41:49+00:00
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        islands = 0 

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return 

            
            # set nodes as visited
            grid[row][col] = '0'

            for dr, dc in directions:
               dfs(row + dr, col + dc)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)

        return islands






        