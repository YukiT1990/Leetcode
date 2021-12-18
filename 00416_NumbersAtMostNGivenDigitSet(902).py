# 902. Numbers At Most N Given Digit Set

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # a. At first we find out all the numbers that can be constructed that have length of less than n.
        # b. Then we count the numbers with the length same as n that can be constructed from digits.
        digits = set(map(int, digits))
        sn = str(n)
        ln = len(sn)

        cnt = 0

        for l in range(1, ln):
            cnt += len(digits) ** l

        for i, dn in enumerate(sn):
            dn = int(dn)
            # all leading digits that are less than current are valid
            less_than = sum(d < dn for d in digits)
            cnt += less_than * len(digits) ** (ln - i - 1)
            if dn not in digits:
                break
            elif i == ln - 1:
                cnt += 1

        return cnt
