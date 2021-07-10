# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0 or s.isspace():
            return 0

        x = s.split()
        return len(x[-1])
