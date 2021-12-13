# 1446. Consecutive Characters

class Solution:
    def maxPower(self, s: str) -> int:
        result = 1
        temp = 0
        i = 1
        while i < len(s):
            if s[i] == s[i-1]:
                temp = 2
                if i == len(s)-1:
                    result = max(result, temp)
                    return result
                while s[i] == s[i+1]:
                    temp += 1
                    i += 1
                    if i == len(s)-1:
                        result = max(result, temp)
                        return result
                if s[i] != s[i+1]:
                    result = max(result, temp)
                    temp = 0

            i += 1
        return result
