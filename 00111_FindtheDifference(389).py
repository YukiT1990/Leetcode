# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s.strip())
        t = list(t.strip())
        for c in s:
            t.remove(c)
        return t[0]