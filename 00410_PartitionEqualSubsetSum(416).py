# 416. Partition Equal Subset Sum

# Reference
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/609458/Python3-2-lines-32ms-bitset-solution-Partition-Equal-Subset-Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, r = divmod(sum(nums), 2)
        return r == 0 and (reduce(lambda x, y: x << y | x, [1] + nums) >> target) & 1
