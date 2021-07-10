# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        import string
        alphabet = string.ascii_uppercase
        dic = {}
        for i, char in enumerate(alphabet):
            dic[char] = i + 1

        result = 0

        for digit, char in enumerate(columnTitle[::-1]):
            result += dic[char] * (26 ** digit)

        return result
