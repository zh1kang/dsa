class TicTacToe:

    def __init__(self, n: int):
        self.grid = [[0] * n for _ in range(n)]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        

    def move(self, row: int, col: int, player: int) -> int:
        
        if self.grid[row][col] == 0:
            self.grid[row][col] = player
        
        return self.checkWin(player, self.grid)
    

    def checkWin(self, player, board):
        # the conditions for winning are: 3 in a row, or 3 diagonal in either direction
        
        # check horiontal rows
        for r in range(self.rows):
            for c in range(self.cols - 2):
                if board[r][c] == player and board[r][c + 1] == player and board[r][c + 2] == player:
                    return player

        # check vertical columns
        for r in range(self.rows - 2):
            for c in range(self.cols):
                if board[r][c] == player and board[r + 1][c] == player and board[r + 2][c] == player:
                    return player

        # check diagonals top left to bottom right
        for r in range(self.rows - 2):
            for c in range(self.cols - 2):
                if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player:
                    return player
        # check diagonal bottom left to top right
        for r in range(2, self.rows):
            for c in range(self.cols - 2):
                if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player:
                    return player
                

        return 0

        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# submission 2180860451 - 2026-10-24T20:55:43+00:00
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag= 0
        

    def move(self, row: int, col: int, player: int) -> int:
        # player 1 = + 1, player 2 = - 1
        val = 1 if player == 1 else -1

        self.rows[row] += val
        self.cols[col] += val

        if row == col:
            self.diag += val
        
        if row + col == self.n - 1:
            self.anti_diag += val


        # check winner
        if (abs(self.rows[row] == self.n) or abs(self.cols[col] == self.n)
        or abs(self.diag) == self.n or abs(self.anti_diag) == self.n):
        return player

        return 0
        
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# submission 2180860512 - 2026-10-24T20:55:52+00:00
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag= 0
        

    def move(self, row: int, col: int, player: int) -> int:
        # player 1 = + 1, player 2 = - 1
        val = 1 if player == 1 else -1

        self.rows[row] += val
        self.cols[col] += val

        if row == col:
            self.diag += val
        
        if row + col == self.n - 1:
            self.anti_diag += val


        # check winner
        if (abs(self.rows[row] == self.n) or abs(self.cols[col] == self.n)
        or abs(self.diag) == self.n or abs(self.anti_diag) == self.n):
            return player

        return 0
        
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# submission 2180860705 - 2026-10-24T20:56:23+00:00
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag= 0
        

    def move(self, row: int, col: int, player: int) -> int:
        # player 1 = + 1, player 2 = - 1
        val = 1 if player == 1 else -1

        self.rows[row] += val
        self.cols[col] += val

        if row == col:
            self.diag += val
        
        if row + col == self.n - 1:
            self.anti_diag += val


        # check winner
        if (abs(self.rows[row] == self.n) or abs(self.cols[col]) == self.n
        or abs(self.diag) == self.n or abs(self.anti_diag) == self.n):
            return player

        return 0
        
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# submission 2180860989 - 2026-10-24T20:57:05+00:00
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag= 0
        

    def move(self, row: int, col: int, player: int) -> int:
        # player 1 = + 1, player 2 = - 1
        val = 1 if player == 1 else -1

        self.rows[row] += val
        self.cols[col] += val

        if row == col:
            self.diag += val
        
        if row + col == self.n - 1:
            self.anti_diag += val


        # check winner
        if (abs(self.rows[row]) == self.n or 
        abs(self.cols[col]) == self.n or 
        abs(self.diag) == self.n or 
        abs(self.anti_diag) == self.n):
            return player

        return 0
        
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)