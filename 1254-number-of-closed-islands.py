class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
    

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0, -1)]

        # flood fill 
        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return

            # set as visited
            grid[r][c] = 1

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        

        # then we check and make sure that the zeros are not on the border if thy are we flood fill them 
        for r in range(rows):
            for c in range(cols):

                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    dfs(r,c)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r,c)

        return count


        

                



        

# submission 2181496211 - 2026-10-25T15:17:52+00:00
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
    

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0, -1)]

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return

            # set as visited
            grid[r][c] = 1

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        

        # then we check and make sure that the zeros are not on the border if thy are we flood fill them 
        for r in range(rows):
            for c in range(cols):

                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    dfs(r,c)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r,c)

        return count


        

                



        
