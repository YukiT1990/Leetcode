# 317. Shortest Distance from All Buildings

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
#         empty_lands = []
#         buildings = []
#         obstacles = []
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == 0:
#                     empty_lands.append([i, j])
#                 elif grid[i][j] == 1:
#                     buildings.append([i, j])
#                 else:
#                     obstacles.append([i, j])
                    
#         path = float('inf')
#         # print(empty_lands)
#         for i, j in empty_lands:
#             temp_path = 0
#             for ib, jb in buildings:
#                 dist = abs(i-ib) + abs(j-jb)
#                 temp_path += dist
#             path = min(path, temp_path)
#         if path != float('inf'):
#             return path
#         else:
#             return -1
        
        
        # Reference
        # https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/918010/Easy-to-understand-Python-3
        cells = [set(), set(), set()]
        
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                cells[c].add((i, j))
        
        empty, buildings, obstacles = cells
		
		# count keeps how many buildings can reach this empty cell
		# distance keeps the distance from all reachable buildings
        count, distances = Counter(), Counter()
        
        for x, y in buildings:
            level, seen, step = [(x, y)], set(), 0
            while level:
                step += 1
                new_level = []
                for i, j in level:
                    for cell in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if cell in empty and cell not in seen:
                            count[cell] += 1
                            distances[cell] = distances[cell] + step
                            seen.add(cell)
                            new_level.append(cell)
                level = new_level
                
        return min([d for c, d in distances.items() if count[c] == len(buildings)] or [-1])
        