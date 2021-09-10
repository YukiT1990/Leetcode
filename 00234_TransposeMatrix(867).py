# 867. Transpose Matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        # print(result)
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                result[c][r] = matrix[r][c]
        return result
    
        # Reference
        # https://leetcode.com/problems/transpose-matrix/discuss/718066/Python-Very-Easy-to-Understand-Solution
        # return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]