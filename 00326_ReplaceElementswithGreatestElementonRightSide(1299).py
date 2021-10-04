# 1299. Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr
    

        # Reference
        # https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/discuss/478465/Python-3-Faster-than-99.7-Memory-less-than-100
        # out = [-1]
        # greatest = 0
        # for num in arr[::-1]:
        #     if greatest < num:
        #         greatest = num
        #     out.append(greatest)
        # out.pop()
        # return out[::-1]