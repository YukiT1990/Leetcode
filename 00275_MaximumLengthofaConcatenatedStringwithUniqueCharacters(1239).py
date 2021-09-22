# 1239. Maximum Length of a Concatenated String with Unique Characters

# Reference
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/631245/Python-3-Easy-Code-Intutive-Solution

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        uniqElements = ['']
        maximum = 0
        for i in range(len(arr)):
            sz = len(uniqElements)
            for j in range(sz):
                x=arr[i]+uniqElements[j]
                if (len(x)==len(set(x))):
                    uniqElements.append(x)
                    maximum = max(maximum, len(x))
                    
        return maximum