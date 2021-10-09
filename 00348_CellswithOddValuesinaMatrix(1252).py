# 1252. Cells with Odd Values in a Matrix

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        dict_row = dict()
        dict_col = dict()
        for r, c in indices:
            if r not in dict_row.keys():
                dict_row[r] = 1
            else:
                dict_row[r] += 1
                
            if c not in dict_col.keys():
                dict_col[c] = 1
            else:
                dict_col[c] += 1
                
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        result = 0
        
        for r in range(m):
            for c in range(n):
                if r in dict_row.keys():
                    matrix[r][c] += dict_row[r]
                if c in dict_col.keys():
                    matrix[r][c] += dict_col[c]
                if matrix[r][c] % 2 != 0:
                    result += 1
        # print(matrix)
        
        return result
        
        
            