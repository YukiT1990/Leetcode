# 292. Nim Game

class Solution:
    def canWinNim(self, n: int) -> bool:
        # if n can be devided by 4, the result is false
        return n % 4