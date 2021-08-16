# 265. Paint House II
# Reference
# https://leetcode.com/problems/paint-house-ii/discuss/535934/Extremely-Concise-REAL-O(kn)-Running-time-O(1)-Space-algorithm-Python

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # res: used to store the smallest and second smallest cost in previous house
        # curRes: used to store the smallest and second smallest cost in current house
        # smallest and second smallest cost are in [position, cost sum] format
        res = [[-1, 0], [-1, 0]]
        for x in costs:
            curRes = [[-1, float('Inf')], [-1, float('Inf')]]
            for i, y in enumerate(x):
                if i != res[0][0]:
                    temp = y + res[0][1]
                else:
                    temp = y + res[1][1]
                if temp < curRes[0][1]:
                    curRes[1] = curRes[0]
                    curRes[0] = [i, temp]
                elif temp < curRes[1][1]:
                    curRes[1] = [i, temp]
            res = curRes
        return res[0][1]
