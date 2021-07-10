# 168. Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        import string
        alphabet = string.ascii_uppercase

        result = ""

        # from desimal into A1 notation
        while columnNumber > 0:
            columnNumber -= 1

            columnNumber, i = divmod(columnNumber, 26)
            result += alphabet[i]

        return result[::-1]
