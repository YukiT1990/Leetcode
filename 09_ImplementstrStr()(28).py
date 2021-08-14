# 28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lengthH = len(haystack)
        lengthN = len(needle)
        if lengthN == 0:
            return 0

        for i in range(lengthH - lengthN + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
