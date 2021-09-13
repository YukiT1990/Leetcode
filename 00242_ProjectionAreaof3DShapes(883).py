# 883. Projection Area of 3D Shapes

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy = 0
        yz = 0
        zx = 0
        y = [0 for _ in range(n)]
        for i in range(n):
            yz += max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    xy += 1
                y[j] = max(y[j], grid[i][j])
        zx = sum(y)
        return xy + yz + zx
            
            
        