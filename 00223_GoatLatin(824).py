# 824. Goat Latin

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        word_list = list(sentence.split(' '))
        
        for i in range(len(word_list)):
            if word_list[i][0] in vowels:
                word_list[i] += 'ma'
            else:
                word_list[i] = word_list[i][1:] + word_list[i][0] + 'ma'
            word_list[i] += 'a' * (i + 1)
        return ' '.join(word_list)