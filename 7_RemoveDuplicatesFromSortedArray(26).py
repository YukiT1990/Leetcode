# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        originalLength = len(nums)
        numsWithoutDup = list(set(nums))
        numsWithoutDup.sort()
        currentLength = len(numsWithoutDup)

        nums.clear()
        for v in numsWithoutDup:
            nums.append(v)

        return currentLength
