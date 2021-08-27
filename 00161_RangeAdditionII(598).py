# 598. Range Addition II

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # 111 ms	16.2 MB
        if not ops:
            return m * n
        minX = m
        minY = n
        for x, y in ops:
            minX = min(minX, x)
            minY = min(minY, y)
        return minX * minY
    
        # 64 ms	16.2 MB
        # Reference
        # https://leetcode.com/problems/range-addition-ii/discuss/380432/Solution-in-Python-3-(one-line)-(beats-~98)
        # return min([i[0] for i in ops])*min([i[1] for i in ops]) if ops else m*n