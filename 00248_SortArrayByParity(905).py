# 905. Sort Array By Parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # 100 ms	14.9 MB
        evens = []
        odds = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        return evens + odds
    
        # 118 ms	14.7 MB
        # Reference
        # https://leetcode.com/problems/sort-array-by-parity/discuss/958432/97-Faster-single-line
        # nums.sort(key=lambda x: x&1)
        # return nums