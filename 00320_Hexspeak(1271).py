# 1271. Hexspeak

class Solution:
    def toHexspeak(self, num: str) -> str:
        hexa = hex(int(num))[2:]
        # print(hexa)
        result = ''
        dict_hex = {'a': "A", 'b': "B", 'c': "C", 'd': "D", 'e': "E", 'f': "F", '1': "I", '0': "O"}
        for d in hexa:
            if d in dict_hex.keys():
                result += dict_hex[d]
            else:
                return "ERROR"
        return result