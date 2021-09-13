# 1189. Maximum Number of Balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 200 ms	14.3 MB
        # # b:1, a:1, l:2, o:2, n:1
        # i = 0
        # while True:
        #     if text.count('b') >= i+1 and text.count('a') >= i+1 and text.count('l') >= (i+1)*2 and text.count('o') >= (i+1)*2 and text.count('n') >= i+1:
        #         i += 1
        #     else:
        #         return i
            
            
        # 20 ms	14.5 MB
        # Reference
        # https://leetcode.com/problems/maximum-number-of-balloons/discuss/872099/Python-or-Runtime-24ms-and-Faster-than-98.25
        chars = ['b', 'a', 'l', 'o', 'n']
        counts = [0 for _ in range(5)]
        
        for i in range(5):
            counts[i] = text.count(chars[i])
            
        counts[2] //= 2
        counts[3] //= 2
        
        return min(counts)
            