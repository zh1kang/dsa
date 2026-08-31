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
            


