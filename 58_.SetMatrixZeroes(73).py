# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_0 = set()
        column_0 = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_0.add(i)
                    column_0.add(j)
        for i in row_0:
            matrix[i] = [0] * len(matrix[i])
        for j in column_0:
            for i in range(len(matrix)):
                matrix[i][j] = 0
