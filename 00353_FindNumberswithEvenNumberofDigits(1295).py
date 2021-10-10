# 1295. Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums = list(map(str, nums))
        return len([x for x in nums if len(x) % 2 == 0])