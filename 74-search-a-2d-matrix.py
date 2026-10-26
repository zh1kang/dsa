class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        # simple binary search but with a 2d matrix
        # high should be r*c - 1
        # for the conditions we check if the current mid value is greater than the end value of the curr row if it is we shift to the next row, if it is less than we shift the high down to the current row 

        r, c = len(matrix), len(matrix[0])

        lo, hi = 0, r*c - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            row = mid // c
            col = mid % c 

            mid_val = matrix[row][col]

            if mid_val == target:
                return True

            if mid_val < target:
                lo = mid + 1

            elif mid_val > target: 
                hi = mid - 1

        return False 

           

            






        