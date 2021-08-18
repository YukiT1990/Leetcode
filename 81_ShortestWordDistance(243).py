# 243. Shortest Word Distance

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # 60 ms	17.6 MB
        index_word1 = []
        index_word2 = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                index_word1.append(i)
            elif wordsDict[i] == word2:
                index_word2.append(i)
        min_diff = len(wordsDict)
        for num1 in index_word1:
            for num2 in index_word2:
                min_diff = min(min_diff, abs(num1 - num2))
        return min_diff
    
        # 68 ms	18 MB
        # index_word1 = -1
        # index_word2 = -1
        # min_diff = len(wordsDict)
        # for i in range(len(wordsDict)):
        #     if wordsDict[i] == word1:
        #         index_word1 = i
        #     elif wordsDict[i] == word2:
        #         index_word2 = i
        #     if index_word1 != -1 and index_word2 != -1:
        #         min_diff = min(min_diff, abs(index_word1 - index_word2))
        # return min_diff
        
    