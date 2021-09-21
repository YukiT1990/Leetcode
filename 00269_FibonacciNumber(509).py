# 509. Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        record = [0 for _ in range(n+1)]
        record[1] = 1
        for i in range(2, n+1):
            record[i] = record[i-1] + record[i-2]
        return record[n]