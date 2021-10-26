# 1370. Increasing Decreasing String

class Solution:
    def sortString(self, s: str) -> str:
        length = len(s)
        s_dict = dict()
        for c in s:
            if c in s_dict.keys():
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        inc = sorted(list(set(s)))
        dec = inc[::-1]

        result = ''
        count = 0
        while True:
            for i in inc:
                if count == length:
                    return result
                if s_dict[i] > 0:
                    result += i
                    s_dict[i] -= 1
                    count += 1
            for i in dec:
                if count == length:
                    return result
                if s_dict[i] > 0:
                    result += i
                    s_dict[i] -= 1
                    count += 1
