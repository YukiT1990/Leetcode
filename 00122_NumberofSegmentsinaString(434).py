# 434. Number of Segments in a String

class Solution:
    def countSegments(self, s: str) -> int:
        if not s or s.isspace():
            return 0
        array = s.strip().split(' ')
        count = 0
        for word in array:
            if len(word) != 0 and not word.isspace() and word != '':
                count += 1
        return count