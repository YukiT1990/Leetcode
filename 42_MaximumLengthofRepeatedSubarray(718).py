# 718. Maximum Length of Repeated Subarray

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        # m rows, n columns
        matrix = [[0 for i in range(n + 1)] for j in range(m + 1)]
        result = 0

        for j in range(m - 1, -1, -1):  # iterate nums2
            for i in range(n - 1, -1, -1): # iterate nums1
                if nums1[i] == nums2[j]:
                    matrix[j][i] = matrix[j + 1][i + 1] + 1
                    result = max(result, matrix[j][i])

        return result
