class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # we want to essentially dfs fro mall the spots with numbers to find the number of islands
        # then we sum the islands and divide by k and then return the number of isalnds that % k == 0.
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            curr_val = grid[r][c]
            # mark as visited
            grid[r][c] = 0
            island_sum = curr_val
            for dr, dc in directions:
                island_sum += dfs(r + dr, c + dc)

        
            return island_sum

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    island_sum = dfs(r,c)
                    if island_sum % k == 0:
                        count += 1

        return count 
                   

                
        
            
        