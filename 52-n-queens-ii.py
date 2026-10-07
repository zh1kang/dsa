class Solution:
    def totalNQueens(self, n: int) -> int:
        # thoughts:
        # we don't need to return the entire board
        # but it is still backtracking

        def backtrack(row, pos_diag, neg_diag, col):
            if row == n:
                return 1
            
            solutions = 0

            for c in range(n):
                curr_pos_diag = row + c
                curr_neg_diag = row - c 
                # if they can attack each other skip
                if c in col or curr_pos_diag in pos_diag or curr_neg_diag in neg_diag:
                    continue 
                
                # add them
                col.add(c)
                pos_diag.add(curr_pos_diag)
                neg_diag.add(curr_neg_diag)

                solutions += backtrack(row + 1, pos_diag, neg_diag, col)

                col.remove(c)
                pos_diag.remove(curr_pos_diag)
                neg_diag.remove(curr_neg_diag)
            
            return solutions

        return backtrack(0, set(), set(), set())






