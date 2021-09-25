# 1065. Index Pairs of a String

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        words = sorted(words, key=lambda x: len(x))
        result = []
        for word in words:
            index = -1
            end = -1
            while word in text[index+1:]:
                index = text[index+1:].find(word) + index + 1
                # print(index)
                end = index + len(word) - 1
                # print(end)
                result.append([index, end])
                
        result = sorted(result, key=lambda x: x[0])
        return result