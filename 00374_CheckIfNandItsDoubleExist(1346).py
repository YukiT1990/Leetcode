# 1346. Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        # print(arr)
        for i in range(len(arr)):
            if arr[i] >= 0:
                if arr[i] * 2 in arr[i+1:]:
                    return True 
            else:
                if arr[i] * 2 in arr[:i]:
                    return True
        return False