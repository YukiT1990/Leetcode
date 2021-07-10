# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        basket = set()
        for num in nums:
            if not num in basket:
                basket.add(num)
            else:
                basket.remove(num)
        return basket.pop()
