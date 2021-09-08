# 830. Positions of Large Groups

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0
        end = 0
        i = 0
        found = False
        while i < len(s) - 1:
            if not found and s[i] == s[i+1]:
                found = True
                start = i
            elif found and s[i] != s[i+1]:
                end = i
                if end - start > 1:
                    result.append([start, end])
                found = False
            if i == len(s) - 2 and found and s[i] == s[i+1]:
                end = i + 1
                if end - start > 1:
                    result.append([start, end])
            i+=1
        return result