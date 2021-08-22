# 459. Repeated Substring Pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 940 ms	14.2 MB
        i = 1
        found = False
        while i <= len(s) // 2:
            if len(s) % i == 0:
                if len(set(s[:i])) != len(set(s)):
                    i += 1
                    continue
                for j in range(0, len(s), i):
                    for k in range(i):
                        if (s[k] != s[j + k]):
                            break
                        if j == len(s) - i and k == i - 1:
                            found = True
            i += 1
        return found
    
        # 47 ms	14.3 MB
        # Reference
        # https://leetcode.com/problems/repeated-substring-pattern/discuss/826151/Python-by-fold-and-find-w-Simple-proof
        # s_fold = "".join( (s[1:], s[:-1]) )
        # return s in s_fold