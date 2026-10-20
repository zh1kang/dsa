class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # thoughts:
        # we can use bfs to find the minimum distance of a theif to any of the nodes
        # and then we can use dijkstras to essentially prune the shortest distances in order to get the maximum safetness factor of a path
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # if the start or end has a we just return 0 
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        # bfs 
        thief_dist = [[-1] * n for _ in range(n)]
        queue = deque()

        # initiallize all the thief distances to 0 and append the locations to queue
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    thief_dist[r][c] = 0

        # find the minimum distance of the thieves to each cell
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and thief_dist[nr][nc] == -1:
                    thief_dist[nr][nc] = thief_dist[r][c] + 1
                    queue.append((nr,nc))


        # dijkstra's: we use a max heap to find the path that maximizes the distance between any cell and the thieves

        # heap should be initialized with the largest distance and the location of it 
        max_heap = [(-thief_dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while max_heap:
            neg_safeness, r, c = heapq.heappop(max_heap)
            curr_safeness = -neg_safeness

            if r == n - 1 and c == n - 1:
                return curr_safeness

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True

                    next_safeness = min(curr_safeness, thief_dist[nr][nc])

                    heapq.heappush(max_heap, (-next_safeness, nr, nc))


        return 0 

                

# submission 2176609782 - 2026-10-19T21:45:13+00:00
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # thoughts:
        # we can use bfs to find the minimum distance of a theif to any of the nodes
        # and then we can use dijkstras to essentially prune the shortest distances in order to get the maximum safetness factor of a path
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # if the start or end has a we just return 0 
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        # bfs 
        thief_dist = [[-1] * n for _ in range(n)]
        queue = deque()

        # initiallize all the thief distances to 0 and append the locations to queue
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    thief_dist[r][c] = 0

        # find the minimum distance of the thieves to each cell
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and thief_dist[nr][nc] == -1:
                    thief_dist[nr][nc] = thief_dist[r][c] + 1
                    queue.append((nr,nc))


        # dijkstra's: we use a max heap to find the path that maximizes the distance between any cell and the thieves

        # heap should be initialized with the largest distance and the location of it 
        best = [[-1] * n for _ in range(n)]
        best[0][0] = thief_dist[0][0]

        max_heap = [(-best[0][0], 0, 0)]

        while max_heap:
            neg_safe, r, c = heapq.heappop(max_heap)
            curr_safe = -neg_safe

            if curr_safe < best[r][c]:
                continue

            if r == n - 1 and c == n - 1:
                return curr_safe

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    next_safe = min(curr_safe, thief_dist[nr][nc])

                    if next_safe > best[nr][nc]:
                        best[nr][nc] = next_safe
                        heapq.heappush(max_heap, (-next_safe, nr, nc))

        return 0