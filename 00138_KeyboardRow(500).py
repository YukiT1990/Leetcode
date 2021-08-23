# 500. Keyboard Row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row_set = set(list("qwertyuiop".strip()))
        second_row_set = set(list("asdfghjkl".strip()))
        third_row_set = set(list("zxcvbnm".strip()))
        
        i = 0
        while i < len(words):
            word_set = set(list(words[i].lower().strip()))
            # print(word_set)
            # print(word_set.issubset(second_row_set))
            if not word_set.issubset(first_row_set) and not  word_set.issubset(second_row_set) and not  word_set.issubset(third_row_set):
                words.remove(words[i])
            else:
                i += 1
        return words
            