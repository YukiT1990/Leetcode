# 442. Find All Duplicates in an Array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dp = [0 for _ in range(max(nums)+1)]
        # print(dp)
        for i in range(len(nums)):
            dp[nums[i]] += 1
        # result = []
        # for i in range(len(dp)):
        #     if dp[i] > 1:
        #         result.append(i)
        # return result
        return [i for i in range(len(dp)) if dp[i] > 1]