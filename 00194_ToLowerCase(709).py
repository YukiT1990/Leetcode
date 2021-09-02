# 709. To Lower Case

class Solution:
    def toLowerCase(self, s: str) -> str:
        # 43 ms	14.3 MB
        # return s.lower()
    
        # faster solusion
        # 32 ms	14.1 MB
        # https://leetcode.com/problems/to-lower-case/discuss/1227317/JS-Python-Java-C%2B%2B-or-Easy-ASCII-Solution-w-Explanation
        ans = ""
        for c in s:
            n = ord(c)
            ans += chr(n+32) if n > 64 and n < 91 else c
        return ans