# 312. Burst Balloons

# Reference
# https://leetcode.com/problems/burst-balloons/discuss/248527/python-DP-solution

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for i in range(N+2)] for j in range(N+2)]
        for l in range(1, N+1):
            for start in range(1, N+1):
                end = start + l - 1
                if end > N:
                    break
                if l == 1:
                    dp[start][end] = nums[start-1]*nums[start]*nums[start+1]
                else:
                    max_ = 0
                    for last in range(start, end+1):
                        v = dp[start][last-1] + dp[last+1][end] + \
                            nums[start-1]*nums[last]*nums[end+1]
                        if v > max_:
                            max_ = v
                    dp[start][end] = max_
        return dp[1][N]
