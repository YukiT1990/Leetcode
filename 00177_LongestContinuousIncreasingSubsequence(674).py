# 674. Longest Continuous Increasing Subsequence

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 0
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                longest = max(longest, count)
                count = 0
            if i == len(nums) - 2:
                longest = max(longest, count)
        return longest + 1
        