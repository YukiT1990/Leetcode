# 819. Most Common Word

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 40 ms	14 MB
        word_dict = dict()
        punc = '''!()-[]{};:'"\<>,./?@#$%^&*_~'''
        for c in paragraph:
            if c in punc:
                paragraph = paragraph.replace(c, ' ')
        word_list = list(re.split(' ', paragraph))
        # print(word_list)
        for word in word_list:
            word = word.lower()
            if word not in banned and word != '':
                word_dict[word] = word_dict.get(word, 0) + 1
        # print(word_dict)
        max_occur = max(word_dict.values())
        for k, v in word_dict.items():
            if v == max_occur:
                return k
            

        # 36 ms	14.1 MB
        # Reference
        # https://leetcode.com/problems/most-common-word/discuss/823208/Python-simple-and-clean-explained-solution
        # my_dict = defaultdict(int)
        # # split string into list ignoring cases and punctuation
        # par = re.split("[" + string.punctuation + " "+ "]+", paragraph.lower())
        # # keep counts of words in dict and keep track of most frequent
        # max_count = 0
        # max_word = ""
        # for word in par:
        #     if word not in banned:
        #         my_dict[word]+=1
        #         if my_dict[word] > max_count:
        #             max_count = my_dict[word]
        #             max_word = word
        # return max_word