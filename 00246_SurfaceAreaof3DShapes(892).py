# 892. Surface Area of 3D Shapes

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # 164 ms	14.2 MB
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    result += 2
                if i-1 < 0:
                    result += grid[i][j]
                else:
                    if grid[i][j] > grid[i-1][j]:
                        result += grid[i][j] - grid[i-1][j]
                if i+1 >= len(grid):
                    result += grid[i][j]
                else:
                    if grid[i][j] > grid[i+1][j]:
                        result += grid[i][j] - grid[i+1][j]
                if j-1 < 0:
                    result += grid[i][j]
                else:
                    if grid[i][j] > grid[i][j-1]:
                        result += grid[i][j] - grid[i][j-1]
                if j+1 >= len(grid[i]):
                    result += grid[i][j]
                else:
                    if grid[i][j] > grid[i][j+1]:
                        result += grid[i][j] - grid[i][j+1]
        return result
    
    
        # 80 ms	14.4 MB
        # Reference
        # https://leetcode.com/problems/surface-area-of-3d-shapes/discuss/930130/More-clear-python-solution
        # N = len(grid)
        # ret = 0
        # for i in range(N):
        #     for j in range(N):
        #         v = grid[i][j]
        #         if v:
        #             ret += 2
        #             ret += v * 4
        #             if i:
        #                 p = grid[i-1][j]
        #                 ret -= min(v, p) * 2
        #             if j:
        #                 p = grid[i][j-1]
        #                 ret -= min(v, p) * 2
        # return ret