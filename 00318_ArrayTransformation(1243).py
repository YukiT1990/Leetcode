# 1243. Array Transformation

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True
        while changed:
            changed = False
            cur_array = arr.copy()
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    changed = True
                    cur_array[i] += 1
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    changed = True
                    cur_array[i] -= 1
            arr = cur_array
        return arr