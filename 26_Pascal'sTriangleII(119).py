# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []

        for i in range(rowIndex + 1):
            currentArray = []
            if i == 0:
                currentArray = [1]
            else:
                currentArray.append(1)
                for j in range(i - 1):
                    currentArray.append(result[i - 1][j] + result[i - 1][j + 1])
                currentArray.append(1)
            result.append(currentArray)
        return result[rowIndex]
