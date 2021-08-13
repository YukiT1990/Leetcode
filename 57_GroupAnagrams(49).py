# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in word_dict:
                word_dict[sorted_word] = [word]
            else:
                word_dict[sorted_word].append(word)
        result = []
        for values in word_dict.values():
            result.append(values)
        return result
