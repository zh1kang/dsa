class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # thoughts:
        # would we use dijkstras to find the shortest path, and then the minimum time we reach the bottom right square is just the largest value on our shortest path since we have to wait until t is equal to t so that it is reachable
        # but in this case wearen't minimizing edge eights but we are minimizing the elevation of the water that we traverse through because we want to wait the shortest amount of time to reach the bottom 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        row, col = len(grid), len(grid[0])

        if row == 0 or col == 0: 
            return 0

        # initialize the min height for the entire grid to be inf 
        min_height = [[float('inf')] * col for _ in range(row)]

        # initialize our starting point (0,0)
        min_height[0][0] = grid[0][0]

        # initialize pq with (cumulative_cost, row, col)
        pq = [(grid[0][0], 0, 0)]

        while pq: 
            curr_height, r, c = heapq.heappop(pq)
            
            if curr_height > min_height[r][c]:
                continue

            if r == row - 1 and c == col - 1:
                return curr_height

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row and 0 <= nc < col:
                    # if we find a height that is bigger 
                    new_height = max(curr_height, grid[nr][nc])

                    # if we find a new height that is smaller than current min height, we add to pq
                    if new_height < min_height[nr][nc]:
                        min_height[nr][nc] = new_height
                        heapq.heappush(pq, (new_height, nr, nc))

        return min_height[row-1][col-1]


    


