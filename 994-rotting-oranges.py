class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = -1

        while q:
            minutes += 1              
            for _ in range(len(q)):   
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  
                        fresh -= 1
                        q.append((nr, nc))

        return minutes if fresh == 0 else -1
            



# submission 2091026699 - 2026-08-02T07:07:21+00:00
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        
        if fresh == 0:
            return 0
        minutes = -1 

        while queue: 
            level_size = len(queue)
            minutes += 1
            # pop the rotten oranges row, col
            for _ in range(level_size):
                row, col = queue.popleft()


                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh -= 1 
                        queue.append((new_row, new_col))

        return minutes if fresh == 0 else -1






        
        

# submission 2091030025 - 2026-08-02T07:10:27+00:00
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        
        if fresh == 0:
            return 0

        minutes = -1 

        while queue: 
            level_size = len(queue)
            minutes += 1
            # pop the rotten oranges (row, col)
            for _ in range(level_size):
                row, col = queue.popleft()

                # search a level (in this case the adjacent oranges) of the rotten roanges 
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2 # rot the fresh oranges next to the current rotten oraange
                        fresh -= 1 
                        queue.append((new_row, new_col)) # append the coordiates of the new rotten oranges 

        return minutes if fresh == 0 else -1






        
        