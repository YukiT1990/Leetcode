# 163. Missing Ranges

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        result = []

        prev = lower - 1
        for i in range(len(nums) + 1):
            current = nums[i] if i < len(nums) else upper + 1

            if current > prev + 1:
                if prev + 1 < current - 1:
                    result.append(str(prev + 1) + "->" + str(current - 1))
                else:
                    result.append(str(prev + 1))

            prev = current

        return result
