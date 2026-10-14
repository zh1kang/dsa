class Solution:
    def minInsertions(self, s: str) -> int:
        # can we just keep track of how many opening and closing parenthesis we have
        # and then if the closing parenthesis lets say x % 2 != 0, we have to add a closing parenthesis until? and then there are always 2x the closing parenthesis as there are opening parenthesis for validity
        # there are three cases where:
        # ()) is valid 
        # ())( needs 2
        # and ))( needs 3 moves 

        closing_needed = 0
        min_moves = 0

        for char in s:
            if char == '(':
                if closing_needed % 2 == 1:
                    min_moves += 1
                    closing_needed -= 1
                closing_needed += 2

            else:
                closing_needed -= 1
                if closing_needed < 0:
                    min_moves += 1
                    closing_needed = 1

        return min_moves + closing_needed



        