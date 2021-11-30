# 85. Maximal Rectangle

# Reference
# https://leetcode.com/problems/maximal-rectangle/discuss/1304139/Python-O(row*col)-using-histogram

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        histograms = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0:
                    histograms[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]) == 0:
                        histograms[i][j] = 0
                    else:
                        histograms[i][j] = histograms[i-1][j]+int(matrix[i][j])

        def maxArea(arr):
            stack = []
            i = 0
            Max = 0
            while i < len(arr):
                if not stack or arr[i] >= arr[stack[-1]]:
                    stack.append(i)
                    i += 1
                else:
                    a = stack.pop()
                    area = arr[a]*((i-stack[-1]-1) if stack else i)
                    Max = max(area, Max)
            pre = stack[-1]
            while stack:
                a = stack.pop()
                area = arr[a]*((pre-stack[-1]) if stack else pre+1)
                Max = max(area, Max)
            return Max
        k = 0
        for i in histograms:
            k = max(k, maxArea(i))
        return k
