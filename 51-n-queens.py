class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # For N queens, the solution lies in the fact that the only way the queens do not attack each other is that if they are in seperate rows or seperate columns, 
        # there cannot be a queen in the same row or column as another

        # we store them in a hash set since we want each column to be unique
        # and also every diagonal to be unique
        cols = set() 
        pos_diag = set()
        neg_diag = set()
        res = []
        board = [['.'] * n for _ in range(n)]
        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board]) 
                return

            for col in range(n):
                # check if there exists a queen on the diagonal or the column
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                # add the queen
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = 'Q'
                
                # check the next row 
                backtrack(row + 1)
                
                # remove
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return res

            
           
                


        

# submission 2160300796 - 2026-10-02T15:48:20+00:00
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # for each queen, they msut be in a distinct row and column,
        # which means we have to keep track of the positive and negative diagonal because they can traverse those as well, including the rows and columns (their current) position themselves.
        # we can find all solutions by backtracking 
        
        res = []
        board = [['.'] * n for _ in range(n)]
        pos_diag = set() # (row + col)
        neg_diag = set() # (row - col)
        col = set() 

        def backtrack(r):
            # if we reach the end, we copy the entire board
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r-c) in neg_diag:
                    continue

                # place the queen
                board[r][c] = 'Q'
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                # explore next row
                backtrack(r + 1)

                # undo
                board[r][c] = '.'
                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)


        backtrack(0)
        return res 

                

        

        
        