# 806. Number of Lines To Write String

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        decode = {'a': widths[0], 'b': widths[1], 'c': widths[2], 'd': widths[3], 'e': widths[4], 'f': widths[5], 'g': widths[6], 'h': widths[7], 'i': widths[8], 'j': widths[9], 'k': widths[10], 'l': widths[11], 'm': widths[12], 'n': widths[13], 'o': widths[14], 'p': widths[15], 'q': widths[16], 'r': widths[17], 's': widths[18], 't': widths[19], 'u': widths[20], 'v': widths[21], 'w': widths[22], 'x': widths[23], 'y': widths[24], 'z': widths[25]}
        cur_width = 0
        lines = 0
        for c in s:
            if cur_width + decode[c] > 100:
                cur_width = 0
                lines += 1
            cur_width += decode[c]
        return [lines+1, cur_width]