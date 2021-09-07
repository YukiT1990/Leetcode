# 800. Similar RGB Color

class Solution:
    def similarRGB(self, color: str) -> str:
        # 47 ms	14.2 MB
        # 32 ms	14.1 MB
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        base16 = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "aa", "bb", "cc", "dd", "ee", "ff"]
        result = "#"
        for i in range(1, len(color), 2):
            int_num = int(color[i:i+2], base=16)
            left = digits.index(color[i])
            min_diff = 256 ** 2
            temp = 0
            for j in range(max(0, left - 1), len(base16)):
                diff = (int_num - int(base16[j], base=16)) ** 2
                if min_diff > diff:
                    min_diff = diff
                    temp = j
                else:
                    break
            result += base16[temp] 
                
        return result
    
        # 55 ms	14.2 MB
        # Reference
        # https://leetcode.com/problems/similar-rgb-color/discuss/430010/Python3-solution-(100)
        # def fn(c):
        #     candidates = [c[0]*2]
        #     d = int(c[0], 16)
        #     if 1 < d : candidates.append(hex(d-1)[2:]*2)
        #     if d < 14: candidates.append(hex(d+1)[2:]*2)
        #     return min(candidates, key=lambda x: abs(int(x, 16) - int(c, 16)))
        
        # return "#"+fn(color[1:3])+fn(color[3:5])+fn(color[5:7])