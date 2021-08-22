# 453. Minimum Moves to Equal Array Elements

# Reference
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/491656/One-line-Python-solution-with-clear-explanation

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)