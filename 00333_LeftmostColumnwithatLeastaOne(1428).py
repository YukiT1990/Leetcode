# 1428. Leftmost Column with at Least a One

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # matrix = [[0 for _ in range(binaryMatrix.dimensions()[0])] for _ in range(binaryMatrix.dimensions()[1])]
        # # print(matrix)
        # for i in range(binaryMatrix.dimensions()[0]):
        #     for j in range(binaryMatrix.dimensions()[1]):
        #         matrix[j][i] = binaryMatrix.get(i, j)
        # # print(matrix)
        # for i in range(len(matrix)):
        #     if 1 in matrix[i]:
        #         return i
        # return -1
    
    
        # Reference
        # https://leetcode.com/problems/leftmost-column-with-at-least-a-one/discuss/921070/Python-3-ultra-simple-binary-search-by-column
        # column-wise binary search O(cols * log(rows)) time complexity
        
        rows, cols = binaryMatrix.dimensions()
        
        left, right = 0, cols -1
    
        while left <= right:
            # print(left, right)
            
            mid = (left + right) // 2

            seen = any([binaryMatrix.get(r, mid) for r in range(rows)])
            
            if left == right:
                return -1 if not seen else left        
  
            if seen:
                right = mid   
            else:
                left = mid + 1