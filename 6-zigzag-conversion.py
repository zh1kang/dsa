class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s 

        # create 2d array 
        rows = [[] for _ in range(numRows)]
        
        curr_row = 0
        direction = 1 # 1 for down, -1 for up

        for char in s:
            rows[curr_row].append(char)

            # change directions if we hit the top or bottom row
            if curr_row == 0:
                direction = 1

            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction 

        return "".join(["".join(row) for row in rows])



        
      
        