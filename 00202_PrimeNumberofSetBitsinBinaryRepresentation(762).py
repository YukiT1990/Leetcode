# 762. Prime Number of Set Bits in Binary Representation

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def is_prime(num):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        return False
                else:
                    return True
            else:
                return False

        count = 0
        for i in range(left, right+1):
            if is_prime(bin(i).count('1')):
                count += 1
        return count