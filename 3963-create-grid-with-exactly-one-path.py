class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        grid = [['#' for _ in range(n)] for _ in range(m)]

        r, c = 0, 0 
        grid[r][c] = '.'
        while r < m - 1 or c < n - 1:
            
            if c < n - 1:
                c += 1
            elif r < m - 1:
                r += 1


            grid[r][c] = '.'

        return ["".join(row) for row in grid]
        
            
            

# submission 2182674520 - 2026-10-27T01:04:44+00:00
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        return ['.' * n] + ['#' * (n-1) + '.'] * (m-1)