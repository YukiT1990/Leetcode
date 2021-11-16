# 368. Largest Divisible Subset

# Reference
# https://leetcode.com/problems/largest-divisible-subset/discuss/1351834/oror-python-oror-clean-solution

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        dp = [[i] for i in nums]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    dp[i] = dp[j]+[nums[i]]
        return max(dp, key=len)
