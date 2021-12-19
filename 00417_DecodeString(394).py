# 394. Decode String

# Reference
# https://leetcode.com/problems/decode-string/discuss/1400105/98-faster-oror-With-and-without-Stack-oror-Cleane-and-Concise

class Solution:
    def decodeString(self, s: str) -> str:
        res, num = "", 0
        stack = []
        for l in s:
            if l.isdigit():
                num = num * 10 + int(l)
            elif l == "[":
                stack.append(res)
                stack.append(num)
                res = ""
                num = 0
            elif l == "]":
                pnum = stack.pop()
                pstr = stack.pop()
                res = pstr + pnum*res
            else:
                res += l
        return res
