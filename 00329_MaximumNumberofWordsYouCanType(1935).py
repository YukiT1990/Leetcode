# 1935. Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(' ')
        # print(text)
        result = 0
        for word in text:
            found = False
            for c in word:
                if c in brokenLetters:
                    found = True
                    break
            if found == False:
                result += 1
        return result
            