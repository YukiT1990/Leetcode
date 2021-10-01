# 1143. Longest Common Subsequence

# Reference
# https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return self.helper(text1, text2, 0, 0)
        m = len(text1)
        n = len(text2)
        # memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        # return self.helper(text1, text2, 0, 0, memo)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    memo[row][col] = 1 + memo[row - 1][col - 1]
                else:
                    memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

        return memo[m][n]
    
    # def helper(self, s1, s2, i, j):
    #     if i == len(s1) or j == len(s2):
    #         return 0
    #     if s1[i] == s2[j]:
    #         return 1 + self.helper(s1, s2, i+1, j+1)
    #     else:
    #         return max(self.helper(s1, s2, i+1, j), self.helper(s1, s2, i, j+1))
        
    # def helper(self, s1, s2, i, j, memo):
    #     if memo[i][j] < 0:
    #         if i == len(s1) or j == len(s2):
    #             memo[i][j] = 0
    #         elif s1[i] == s2[j]:
    #             memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
    #         else:
    #             memo[i][j] = max(
    #                 self.helper(s1, s2, i + 1, j, memo),
    #                 self.helper(s1, s2, i, j + 1, memo),
    #             )
    #     return memo[i][j]