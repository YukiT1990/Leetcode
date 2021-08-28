# 1235. Maximum Profit in Job Scheduling

# Reference
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/825799/sort-%2B-DP-with-binary-search-on-the-right-indices..-Fast

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        X = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        startTimeSorted = [x[0] for x in X]
        n = len(X)
        dp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            j = bisect.bisect_left(startTimeSorted, X[i][1], i+1)
            dp[i] = max(dp[i+1], X[i][2] + dp[j])
        # print(dp)
        return dp[0]