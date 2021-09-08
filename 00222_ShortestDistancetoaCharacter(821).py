# 821. Shortest Distance to a Character

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [i for i, x in enumerate(s) if x == c]
        # print(indices)
        result = []
        for i in range(len(s)):
            min_dist = len(s)
            for j in indices:
                min_dist = min(min_dist, abs(j - i))
            result.append(min_dist)
        return result