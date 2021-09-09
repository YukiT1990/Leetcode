# 764. Largest Plus Sign

# Reference
# https://leetcode.com/problems/largest-plus-sign/discuss/393943/Compact-Solution-in-Python-3-(nine-lines)

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        DP, M, m = [[0]*n for i in range(n)], {tuple(m) for m in mines}, 0
        for i in range(n):
            c = 0
            for j in range(n):
                c = 0 if (i, j) in M else c + 1
                DP[i][j] = c
            c = 0
            for j in range(n-1, -1, -1):
                c = 0 if (i, j) in M else c + 1
                DP[i][j] = min(DP[i][j], c)
        for j in range(n):
            c = 0
            for i in range(n):
                c = 0 if (i, j) in M else c + 1
                DP[i][j] = min(DP[i][j], c)
            c = 0
            for i in range(n-1, -1, -1):
                c = 0 if (i, j) in M else c + 1
                m = max(m, min(DP[i][j], c))
        return m