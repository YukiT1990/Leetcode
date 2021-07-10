# 190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        reverseBinN = bin(n)[:1:-1]
        return int(reverseBinN + '0' * (32 - len(reverseBinN)), 2)

        
