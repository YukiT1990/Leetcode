# 296. Best Meeting Point

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Time Limit Exceeded
        # DP, G = [[0] * len(grid[0]) for i in range(len(grid))], []
        # # print(grid)
        # # print(DP)
        # # print(G)
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == 1:
        #             G.append((i, j))
        # # print(G)
        # min_dist = float('inf')
        # for i in range(len(DP)):
        #     for j in range(len(DP[i])):
        #         for k in range(len(G)):
        #             DP[i][j] += (abs(G[k][0] - i) + abs(G[k][1] - j))
        #         min_dist = min(min_dist, DP[i][j])
        # return min_dist
    
    
        # Reference
        # https://leetcode.com/problems/best-meeting-point/discuss/763173/O(mn)-solution-very-similar-with-462.-Minimum-Moves-to-Equal-Array-Elements-II
        m, n = len(grid), len(grid[0])
        row = []
        col = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row.append(i)     # row is sorted already
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    col.append(j)     # col is sorted already

        # Median minimizes the absolute distance of points. Mean minimizes the squared distance from points.
        row_median = row[len(row)//2]
        col_median = col[len(col)//2]

        dist = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist += abs(i - row_median) + abs(j - col_median)
        return dist