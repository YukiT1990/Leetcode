# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        word_num = dict()
        for c in s:
            if c in word_num.keys():
                word_num[c] += 1
            else:
                word_num[c] = 1
        keys = list(word_num.keys())
        # print(keys)
        keys = sorted(keys, key=lambda x: word_num[x], reverse=True)
        # print(keys)
        result = ""
        for k in keys:
            result += k * word_num[k]
        return result