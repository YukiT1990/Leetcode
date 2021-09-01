# 717. 1-bit and 2-bit Characters

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            else:
                if i == len(bits) - 1:
                    return True
                i += 1
        return False
        