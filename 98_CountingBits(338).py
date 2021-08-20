# 338. Counting Bits

# Reference
# https://leetcode.com/problems/counting-bits/discuss/817548/Python-O(n)-The-method-of-DP-and-Bit-manipulation.-Easy-understanding-with-explaination.

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]   # when it's 0
        for i in range(1, n + 1):
            answer.append((i & 1) + answer[i >> 1]) 
        return answer
    # i >> 1: shift to right by 1 bits
    # x & y: becomes 1 when both are 1
    """
    10 & 12 ->

    1010  = 10
    1100  = 12
    ------------
    1000  = 08
    """