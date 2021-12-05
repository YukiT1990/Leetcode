# 1351. Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    result += n - j
                    break
        return result
