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





        