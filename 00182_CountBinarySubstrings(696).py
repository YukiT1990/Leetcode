# 696. Count Binary Substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Time Limit Exceeded
        # max_count = min(s.count('1'), s.count('0'))
        # result = 0
        # for i in range(1, max_count + 1):
        #     target01 = '0'*i + '1'*i
        #     target10 = '1'*i + '0'*i
        #     result += s.count(target01)
        #     result += s.count(target10)
        # return result


        # 155 ms	14.5 MB
        # Reference
        # https://leetcode.com/problems/count-binary-substrings/discuss/776686/Python-Commented-or-O(1)-space
        if not s:
            return 0
        now, flag = 0, s[0]
        prev = 0
        res = 0
        for x in s:
            if x == flag:
                now += 1
            else:
                res += min(now, prev)
                prev = now
                now, flag = 1, x
        res += min(now, prev)
        return res