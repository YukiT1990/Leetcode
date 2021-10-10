# 1304. Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n % 2 == 1:
            arr.append(0)
        for i in range(1, n//2+1):
                arr.append(i)
                arr.append(i*-1)
        return arr