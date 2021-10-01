# 1213. Intersection of Three Sorted Arrays

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr1 = set(arr1)
        arr2 = set(arr2)
        arr3 = set(arr3)
        return sorted(list(arr1.intersection(arr2).intersection(arr3)))