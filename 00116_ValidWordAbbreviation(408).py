# 408. Valid Word Abbreviation

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if abbr.isdigit() and len(word) < int(abbr):
            return False
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            # alphabet
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            # number
            else:
                if abbr[j] == '0':
                    return False
                # two digits
                if abbr[j:j+2].isdigit():
                    i += int(abbr[j:j+2])
                    if i > len(word):
                        return False
                    j += 2
                # one digit
                else:
                    i += int(abbr[j])
                    if i > len(word):
                        return False
                    j += 1
        if j < len(abbr) or i < len(word):
            return False
        return True