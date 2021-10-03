# 1619. Mean of Array After Removing Some Elements

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        # print(arr)
        arr = arr[len(arr)//20:-1*len(arr)//20]
        # print(arr)
        return sum(arr)/len(arr)