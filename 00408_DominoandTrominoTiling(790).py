# 790. Domino and Tromino Tiling

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n+1):
            dp[i] = (dp[i-1] * 2 + dp[i-3]) % (10**9 + 7)
        return dp[n]

        # Reference
        # https://leetcode.com/problems/domino-and-tromino-tiling/discuss/1620809/PythonJAVACC%2B%2B-DP-oror-Visualized-Explanation-oror-100-Faster-oror-O(N)

        # dp = [1, 2, 5] + [0] * n
        # for i in range(3, n):
        #     dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % 1000000007
        # return dp[n - 1]
