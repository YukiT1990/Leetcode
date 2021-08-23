# 492. Construct the Rectangle

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = 1
        divisor = 0
        while i**2 <= area:
            if area % i == 0:
                divisor = max(divisor, i)
            i += 1
        return [area // divisor, divisor]
                