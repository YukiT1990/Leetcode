# 227. Basic Calculator II

# Reference
# https://leetcode.com/problems/basic-calculator-ii/discuss/507990/Python-3-Runtime-76ms-Stack-Approach

class Solution:
    def calculate(self, s: str) -> int:
        num, presign, stack = 0, "+", []
        for i in s+'+':
            if i.isdigit():
                num = num*10 + int(i)
            elif i in '+-*/':
                if presign == '+':
                    stack.append(num)
                if presign == '-':
                    stack.append(-num)
                if presign == '*':
                    stack.append(stack.pop()*num)
                if presign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                presign = i
                num = 0
        return sum(stack)
