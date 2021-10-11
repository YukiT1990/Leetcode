# 1309. Decrypt String from Alphabet to Integer Mapping

class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypt1 = {'10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
        decrypt2 = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i'}
        decoded = ""
        prev = -1
        cur = 0
        while cur < len(s):
            if s[cur] == '#' or cur == len(s) - 1:
                if cur - prev == 3:
                    decoded += decrypt1[s[prev+1:cur+1]]
                elif cur - prev > 3:
                    for i in range(prev+1, cur-2):
                        decoded += decrypt2[s[i]]
                    decoded += decrypt1[s[cur-2:cur+1]]
                else:
                    for i in range(prev+1, cur+1):
                        decoded += decrypt2[s[i]]
                prev = cur
            cur += 1
        return decoded