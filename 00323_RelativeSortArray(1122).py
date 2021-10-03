# 1122. Relative Sort Array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for d in arr2:
            count = arr1.count(d)
            for i in range(count):
                result.append(d)
                arr1.remove(d)
        arr1.sort()
        result += arr1
        return result