# 1287. Element Appearing More Than 25% In Sorted Array

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # 1948 ms	15.9 MB
        N = len(arr)
        arr_set = list(set(arr))
        # print(arr_set)
        for d in arr_set:
            if arr.count(d) > N / 4:
                return d
        
        # 2342 ms	15.9 MB
        # Reference
        # https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/discuss/452166/Python-3-(four-different-one-line-solutions)-(beats-100)
        # return max(set(arr), key=arr.count)