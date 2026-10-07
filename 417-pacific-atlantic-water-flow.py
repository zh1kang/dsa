class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            # out of bounds
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Pacific = top and left
        # Atlantic = bottom and right

        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

# submission 2164419583 - 2026-10-06T15:56:35+00:00
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            # out of bounds
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Pacific = top and left
        # Atlantic = bottom and right

        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res


        # TC: O(m*n)
        # SC: O(m*n)
