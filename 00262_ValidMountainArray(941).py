# 941. Valid Mountain Array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        summit = arr.index(max(arr))
        
        if summit == 0 or summit == len(arr)-1:
            return False
        
        for i in range(summit):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(summit, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True