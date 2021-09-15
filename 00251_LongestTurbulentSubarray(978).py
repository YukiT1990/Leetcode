# 978. Longest Turbulent Subarray

# Reference
# https://leetcode.com/problems/longest-turbulent-subarray/discuss/514387/Straight-forward-python-solution-using-dynamic-programming

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp1 = [1 for _ in range(len(arr))]
        dp2 = [1 for _ in range(len(arr))]
        max_num = 1
        for i in range(len(arr)-1):
            if i%2 == 1 and arr[i] > arr[i+1] or i%2 == 0 and arr[i] < arr[i+1]:
                dp1[i+1] = dp1[i]+1
                if dp1[i+1] > max_num: 
                    max_num = dp1[i+1]
            elif i%2 == 0 and arr[i] > arr[i+1] or i%2 == 1 and arr[i] < arr[i+1]:
                dp2[i+1] = dp2[i]+1
                if dp2[i+1] > max_num: 
                    max_num = dp2[i+1]
        return max_num
            
                