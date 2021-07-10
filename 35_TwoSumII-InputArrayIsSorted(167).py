# 167. Two Sum II - Input array is sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}  # v: i
        for i, v in enumerate(numbers):
            d = target - v
            if d in dic:
                return [dic[d], i+1]
            dic[v] = i + 1
        return None
