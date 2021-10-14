# 279. Perfect Squares

# Reference
# https://leetcode.com/problems/perfect-squares/discuss/1006278/Easy-Python-DP-solution-with-explanation-(Dry-Run)

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        
        for i in range(n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-(j*j)] + 1)
                j += 1
        return dp[-1]