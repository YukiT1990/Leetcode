# 1228. Missing Number In Arithmetic Progression

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        # print(d)
        if d == 0:
            return arr[0]
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] != d:
                return arr[i] + d