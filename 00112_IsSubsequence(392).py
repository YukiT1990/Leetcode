# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in s:
            if c not in t[i:]:
                return False
            else:
                i += t[i:].index(c)
            i += 1
        return True