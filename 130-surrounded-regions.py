class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we can dfs out from the 'O's and if they are surrounded by x's we can capture them, however, we don't dfs on O's that are on the borders becasue they're uncapturable? but like for consecutive O's that are in line can still be captured because the connected component is surrounded. 
        # we are guaranteed that O's that are not on the border are completely enclosed, so I think this will be fine. 
        
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (-0,-1)]

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "X":
                return

            # visited 
            board[r][c] = "T"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # we only want to search the regions that are not the boarders 
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols -1 and board[r][c] == "O":
                    dfs(r, c)

        # capture surrounded O's and restore safe ones

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        

# submission 2181741402 - 2026-10-25T21:09:04+00:00
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we can dfs out from the 'O's and if they are surrounded by x's we can capture them, however, we don't dfs on O's that are on the borders becasue they're uncapturable? but like for consecutive O's that are in line can still be captured because the connected component is surrounded. 
        # we are guaranteed that O's that are not on the border are completely enclosed, so I think this will be fine. 
        
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (-0,-1)]

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "X":
                return

            # visited 
            board[r][c] = "T"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # we only want to search the regions that are not the boarders 
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols -1:
                    if board[r][c] == "O":
                        dfs(r, c)

        # capture surrounded O's and restore safe ones
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        

# submission 2181741865 - 2026-10-25T21:10:21+00:00
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we can dfs out from the 'O's and if they are surrounded by x's we can capture them, however, we don't dfs on O's that are on the borders becasue they're uncapturable? but like for consecutive O's that are in line can still be captured because the connected component is surrounded. 
        # we are guaranteed that O's that are not on the border are completely enclosed, so I think this will be fine. 
        
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (-0,-1)]

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return

            # visited 
            board[r][c] = "T"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # we only want to search the regions that are not the boarders 
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols -1:
                    if board[r][c] == "O":
                        dfs(r, c)

        # capture surrounded O's and restore safe ones
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        