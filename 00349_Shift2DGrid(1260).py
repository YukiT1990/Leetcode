# 1260. Shift 2D Grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        line = []
        for r in grid:
            line += r
        k = k % len(line)
        line = line[k*-1:] + line[:k*-1]
        
        new_grid = []
        for i in range(0, len(line), len(grid[0])):
            new_grid.append(line[i:i+len(grid[0])])
        
        return new_grid