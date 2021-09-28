# 1030. Matrix Cells in Distance Order

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        result = []
        for i in range(0, rows):
            for j in range(0, cols):
                result.append([i, j])
        # print(result)
        result = sorted(result, key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return result