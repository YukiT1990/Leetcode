# 1217. Minimum Cost to Move Chips to The Same Position

# Reference
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/discuss/827645/Don't-overthink-about-it.-This-is-more-of-a-math-problem

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        dp = [p%2 for p in position]
        return min(dp.count(0), dp.count(1))