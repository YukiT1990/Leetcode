# 115. Distinct Subsequences

# Reference
# https://leetcode.com/problems/distinct-subsequences/discuss/690327/Python-Simple-solution-with-Example-and-DP-table.

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        
        for k in range(len(dp)):
            dp[k][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if (s[i-1] == t[j-1] and dp[i-1][j-1]):
                    dp[i][j] = max(dp[i-1][j-1] + dp[i-1][j], dp[i-1][j]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]