# 994. Rotting Oranges

import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 88 ms	14.4 MB
#         minutes = 0
        
#         def has_1(grid):
#             for row in grid:
#                 if 1 in row:
#                     return True
#             return False
        
#         if not has_1(grid):
#             return 0
        
#         while True:
#             changed = False
#             copied_grid = copy.deepcopy(grid)
#             # print(copied_grid)
#             # print(grid)
#             for i in range(len(grid)):
#                 for j in range(len(grid[i])):
#                     if copied_grid[i][j] == 2:
#                         if i-1 >= 0:
#                             if grid[i-1][j] == 1:
#                                 grid[i-1][j] = 2
#                                 changed = True
#                         if j-1 >= 0:
#                             if grid[i][j-1] == 1:
#                                 grid[i][j-1] = 2
#                                 changed = True
#                         if i+1 < len(grid):
#                             if grid[i+1][j] == 1:
#                                 grid[i+1][j] = 2
#                                 changed = True
#                         if j+1 < len(grid[i]):
#                             if grid[i][j+1] == 1:
#                                 grid[i][j+1] = 2
#                                 changed = True
#             minutes += 1
#             if not changed:
#                 if has_1(grid):
#                     return -1
#                 else:
#                     return minutes - 1
                
        # 48 ms	14.3 MB
        # Reference
        # https://leetcode.com/problems/rotting-oranges/discuss/1120339/Two-sets-solution-99-speed.
        fresh = set()
        rotten = set()
        minute = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 1:
                    fresh.add((r, c))
                elif v == 2:
                    rotten.add((r, c))
        while rotten and fresh:
            new_rot = set()
            for r, c in rotten:
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_tpl = (r + i, c + j)
                    if new_tpl in fresh:
                        fresh.remove(new_tpl)
                        new_rot.add(new_tpl)
            rotten = new_rot
            minute += 1
        return minute if not fresh else -1
                
        