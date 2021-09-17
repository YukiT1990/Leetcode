# 914. X of a Kind in a Deck of Cards

# Reference
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/discuss/350904/Solution-in-Python-3-(beats-~99)-(one-line)

from functools import reduce
from math import gcd
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values()) != 1