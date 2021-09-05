# 899. Orderly Queue

# Reference
# https://leetcode.com/problems/orderly-queue/discuss/1350871/Python3-rotation-or-sorting

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return "".join(sorted(s))  # returns "aaabc"
        # return sorted(s) # returns ["a","a","a","b","c"]