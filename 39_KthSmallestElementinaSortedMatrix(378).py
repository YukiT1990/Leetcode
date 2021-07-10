# 378. Kth Smallest Element in a Sorted Matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        longList = []

        for i in range(len(matrix)):
            longList += matrix[i]
            
        longList.sort()

        return longList[k - 1]
