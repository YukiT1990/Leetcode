# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            currentArray = []
            if i == 0:
                currentArray = [1]
            else:
                currentArray.append(1)
                for j in range(i - 1):
                    currentArray.append(result[i - 1][j] + result[i - 1][j + 1])
                currentArray.append(1)
            result.append(currentArray)
        return result
