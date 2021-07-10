# 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_digits = [str(digit) for digit in digits]
        str_of_digits = "". join(string_digits)
        str_of_answer = str(int(str_of_digits) + 1)
        result = [int(c) for c in str_of_answer]
        return result
