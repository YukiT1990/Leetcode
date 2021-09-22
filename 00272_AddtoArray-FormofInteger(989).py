# 989. Add to Array-Form of Integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = list(map(str, num))
        num = int(''.join(num))
        num += k
        num = str(num)
        return list(num.strip())