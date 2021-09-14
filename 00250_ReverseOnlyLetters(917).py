# 917. Reverse Only Letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letter_or_not = []
        letters = []
        for c in s:
            if c.isalpha():
                letter_or_not.append('')
                letters.append(c)
            else:
                letter_or_not.append(c)
        letters.reverse()
        
        for i in range(len(letter_or_not)):
            if letter_or_not[i] != '':
                letters.insert(i, letter_or_not[i])
                
        return ''.join(letters)