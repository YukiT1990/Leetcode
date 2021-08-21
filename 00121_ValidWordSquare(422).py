# 422. Valid Word Square

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        matrix = []
        for word in words:
            matrix.append(list(word.strip()))
        for i in range(len(matrix)):
            if len(matrix) < len(matrix[i]):
                    return False
            for j in range(len(matrix[i])):
                if len(matrix[j]) <= i:
                    return False
                if matrix[i][j] != matrix[j][i]:
                    return False
                
        return True