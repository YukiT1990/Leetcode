# 848. Shifting Letters

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        new_shifts = [sum(shifts)]
        for i in range(1, len(shifts)):
            new_shifts.append(new_shifts[i-1] - shifts[i-1])
        def shift(i: int, c: str):
            index = alphabets.index(c)
            target = (index + i) % 26
            return alphabets[target]
        
        result = ''
        for i in range(len(s)):
            result += shift(new_shifts[i], s[i])
        return result
    
        