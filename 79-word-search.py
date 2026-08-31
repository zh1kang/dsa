class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(col)] for _ in range(rows)]

        def dfs(i, row, col):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= rows or col >= cols or word[i] != board[row][col] or visited[row][col]:
                return False

            visited[row][col] = True
            res = (dfs(i + 1, row + 1, col) or 
                    dfs(i + 1, row - 1, col) or
                    dfs(i+ 1, row, col + 1) or
                    dfs(i + 1, row, col - 1))
            visited[row][col] = False
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True
        

        return False 





        

# submission 1871787918 - 2026-01-02T07:55:35+00:00
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(i, row, col):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= rows or col >= cols or word[i] != board[row][col] or visited[row][col]:
                return False

            visited[row][col] = True
            res = (dfs(i + 1, row + 1, col) or 
                    dfs(i + 1, row - 1, col) or
                    dfs(i+ 1, row, col + 1) or
                    dfs(i + 1, row, col - 1))
            visited[row][col] = False
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True
        

        return False 





        

# submission 2088806394 - 2026-07-31T12:53:10+00:00
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        def backtrack(row, col, index):
            
            if index == len(word):
                return True
            
            if (row < 0 or row >= rows 
                or col < 0 or col >= cols or 
                board[row][col] != word[index]):
                return False

            temp = board[row][col]
            board[row][col] = '#'
            

            found = (backtrack(row + 1, col, index + 1) or
                    backtrack(row - 1, col, index + 1) or 
                    backtrack(row, col + 1, index + 1) or
                    backtrack(row, col - 1, index + 1))

            board[row][col] = temp

            return found 


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True

        return False 



           

            

            
            
            