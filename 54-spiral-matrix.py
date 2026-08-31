class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # this is just matrix traversal, but we always start top left,
        # if we hit a boundary from right -> left, we go down, if we hit a boundry we go left, and if we hit another one we go up, but we have to keep track 
        # of which ones been visited so we dont run in a cycle, and thne if we bump into a visited node we go right so we end the spiral. 

        visited = set() # O(1)
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up 
        res = []

        r, c = 0, 0
        direction = 0 

        for _ in range(rows * cols): #O(m * n)
            # visit current cell
            res.append(matrix[r][c])
            visited.add((r,c))

            dr, dc = directions[direction] 

            # where do we go next
            nr, nc = r + dr, c + dc 

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited:
                direction = (direction + 1) % 4 # % allows us to wrap back around 
                dr, dc = directions[direction]
                nr = r + dr
                nc = c + dc 

            r, c = nr, nc 
        return res 



                


