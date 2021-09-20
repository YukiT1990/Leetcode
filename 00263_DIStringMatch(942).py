# 942. DI String Match

# Reference
# https://leetcode.com/problems/di-string-match/discuss/619851/Very-simple-solution-in-python-with-explanations

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        b, e = 0, len(s)
        res = []
        for c in s:
            if c == 'I':
                res.append(b)
                b += 1
            else:
                res.append(e)
                e -= 1
        res.append(b)
        return res