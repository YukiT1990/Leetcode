# 643. Maximum Average Subarray I

# Reference
# https://leetcode.com/problems/maximum-average-subarray-i/discuss/336428/Solution-in-Python-3-(beats-100)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_diff = diff = 0
        for i in range(len(nums) - k):
            diff += nums[i+k] - nums[i]
            if diff > max_diff:
                max_diff = diff
        return (sum(nums[:k]) + max_diff) / k