# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        appeared = set()
        for i, char in enumerate(s):
            if char in appeared:
                continue
            if s.count(char) == 1:
                return i
            appeared.add(char)
        return -1