# 54. Spiral Matrix

# Reference
# https://leetcode.com/problems/spiral-matrix/discuss/999388/95.41-faster-solution

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            
            matrix = (list(zip(*matrix)))[::-1]
        
        return result
        
# In addition, use * that allows you to unpack the list and pass its elements to the function.
# https://note.nkmk.me/en/python-list-transpose/