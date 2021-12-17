# 221. Maximal Square

# Reference
# https://leetcode.com/problems/maximal-square/discuss/944753/python-DP-probably-without-using-extra-space

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) < 1:
            return 0
        rows, cols, max_size = len(matrix), len(matrix[0]), 0
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = int(matrix[row][col])
                if matrix[row][col] >= 1:
                    if row-1 >= 0 and col-1 >= 0:
                        matrix[row][col] = min(
                            matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1])+1
                    max_size = max(max_size, matrix[row][col])
        return max_size * max_size
