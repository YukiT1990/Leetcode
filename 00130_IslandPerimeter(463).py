# 463. Island Perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 594 ms	14.7 MB
        result = 0
        for i in range(len(grid)):
            num_1 = grid[i].count(1)
            if num_1 > 0:
                count = 0
                start = False
                for j in range(len(grid[i]) - 1):
                    if grid[i][j] == 1:
                        start = True
                    if start and grid[i][j] != grid[i][j + 1]:
                        count += 1
                result += 2 * (count // 2 + 1)
                if i == 0:
                    result += num_1
                if i == len(grid) - 1:
                    result += num_1
            if not i == len(grid) - 1:
                for j in range(len(grid[i])):
                    if grid[i][j] != grid[i + 1][j]:
                        result += 1
        return result
    
        # 479 ms	14.7 MB
        # Reference
        # https://leetcode.com/problems/island-perimeter/discuss/724267/PYTHON-3-Iterative-Solution-or-Easy-to-Read
        # row , col , count = len(grid) , len(grid[0]) , 0
        # for x in range(row):
        #     for y in range(col):
        #         if grid[x][y] == 1:
        #             count += 4
        #             if x > 0 and grid[x - 1][y] == 1:
        #                 count -= 2
        #             if y > 0 and grid[x][y - 1] == 1:
        #                 count -= 2
        # return count