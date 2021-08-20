# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 28 ms	14.2 MB
        # my_guess = n // 2
        # length = n // 2 + 1
        # while (length > 1):
        #     length //= 2
        #     if guess(my_guess) == -1:
        #         my_guess -= length
        #     elif guess(my_guess) == 1:
        #         my_guess += length
        #     else:
        #         return my_guess
        # while True:
        #     if guess(my_guess) == -1:
        #         my_guess -= 1
        #     elif guess(my_guess) == 1:
        #         my_guess += 1
        #     else:
        #         return my_guess
            
        # Binary Search
        # 24 ms	14.2 MB
        left, right = 0, n
        while (left <= right):
            middle = (left + right) // 2
            if guess(middle) == -1:
                right = middle - 1
            elif guess(middle) == 1:
                left = middle + 1
            else:
                return middle