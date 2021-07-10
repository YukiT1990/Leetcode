# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityNum = len(nums) // 2 + 1
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for num in dic:
            if dic[num] >= majorityNum:
                return num
