# 1165. Single-Row Keyboard

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        current = 0
        dist = 0
        for c in word:
            index = keyboard.find(c)
            dist += abs(current - index)
            current = index
        return dist