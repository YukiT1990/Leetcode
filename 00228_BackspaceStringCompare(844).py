# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s.strip())
        t = list(t.strip())
        i = 0
        j = 0
        while i < len(s):
            if s[i] == '#':
                s.pop(i)
                if i - 1 >= 0:
                    s.pop(i-1)
                    i -= 1
            else:
                i += 1
        while j < len(t):
            if t[j] == '#':
                t.pop(j)
                if j - 1 >= 0:
                    t.pop(j-1)
                    j -= 1
            else:
                j += 1
        
        s = ''.join(s)
        t = ''.join(t)
        # print(s)
        # print(t)
        if s == t:
            return True
        else:
            return False