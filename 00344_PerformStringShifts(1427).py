# 1427. Perform String Shifts

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shift = 0
        for drc, amt in shift:
            if drc == 0:
                left_shift += amt
            else:
                left_shift -= amt
        # print(left_shift)
        left_shift = left_shift % len(s)
        if left_shift > 0:
            s = s[left_shift:] + s[:left_shift]
        elif left_shift < 0:
            right_shift = len(s) + left_shift
            s = s[right_shift:] + s[:right_shift]
        return s