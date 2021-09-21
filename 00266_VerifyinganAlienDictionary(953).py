# 953. Verifying an Alien Dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Reference
        # Sorting string values according to a custom alphabet in Python
        # https://stackoverflow.com/questions/26579392/sorting-string-values-according-to-a-custom-alphabet-in-python
        # alphabet = "bafmxpzv"
        # a = ['af', 'ax', 'am', 'ab', 'zvpmf']
        # sorted(a, key=lambda word: [alphabet.index(c) for c in word])
        
        sorted_words = sorted(words, key=lambda word: [order.index(c) for c in word])
        if words == sorted_words:
            return True
        else:
            return False