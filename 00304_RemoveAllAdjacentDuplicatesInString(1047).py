# 1047. Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 248 ms	15.1 MB
#         i = 0
#         while i < len(s) - 1:
#             if s[i] == s[i+1]:
#                 s = s[:i] + s[i+2:]
#                 if i > 0:
#                     i -= 1
#                 else:
#                     i = 0
#             else:
#                 i += 1
                
#         return s
    

        # 72 ms	15.5 MB
        # Reference
        # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/560221/Python-96.79-run-time-100-memory
        if not s:
            return s
        res = [s[0]]
        for curr in s[1:]:            
            if res and curr == res[-1]:
                res.pop()
            else:
                res.append(curr)
        res = ''.join(res)                
        return res