class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we transpose and then reverse the rows

        n = len(matrix)
        for i in range(n):
            # Only iterate over the upper triangle to avoid swapping elements back
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

        return matrix
            