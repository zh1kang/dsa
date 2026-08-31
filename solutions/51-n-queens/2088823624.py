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

            
           
                


        