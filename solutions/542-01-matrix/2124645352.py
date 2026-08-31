class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # nearest = min 
        # we can use multi-source bfs from a cell, if we hit a zero, we just return the current distance for each cell to a zero 

        rows, cols = len(mat), len(mat[0])
        queue = deque()
        dist = [[-1] * cols for _ in range(rows)] # initialize a 2d grid with the distances set at -1 

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r,c))
            

        dir = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in dir:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        return dist 

        # TC: O(RC); Space: O(RC) every cell is visited at most once
        # divergences:
        # had to remember how multisource bfs worked; our initial state and what we're measuring the distance from are the cells that are already 0, which is why we put it into the queue
        # then whatever distance we return must be the min because bfs works level by level


        