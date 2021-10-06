# 1200. Minimum Absolute Difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        # print(arr)
        diff = []
        for i in range(len(arr)-1):
            diff.append(arr[i+1] - arr[i])
        # print(diff)
        min_diff = min(diff)
        result = []
        for i in range(len(diff)):
            if diff[i] == min_diff:
                result.append([arr[i], arr[i+1]])
        return result