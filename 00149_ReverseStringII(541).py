# 541. Reverse String II

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s.strip())
        for i in range(0, len(s), 2 * k):
            if len(s[i:]) < k:
                array = s[i:]
                array.reverse()
                s[i:] = array
            else:
                array = s[i:i+k]
                array.reverse()
                s[i:i+k] = array
                
        return ''.join(s)
            