# 566. Reshape the Matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        long_list = []
        for row in mat:
            long_list += row
        
        result = []
        
        for i in range(0, len(long_list), c):
            result.append(long_list[i:i+c])
            
        return result