# 507. Perfect Number

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        divisors = [1]
        i = 2
        while i ** 2 <= num:
            if num % i == 0:
                divisors.append(i)
                divisors.append(num//i)
            i += 1
        if sum(divisors) == num:
            return True
        else:
            return False
            
        # Reference
        # https://leetcode.com/problems/perfect-number/discuss/373865/Python-99.57-for-crooks-%3A)
        # https://oeis.org/A000396
        # return num in (6, 28, 496, 8128, 33550336)