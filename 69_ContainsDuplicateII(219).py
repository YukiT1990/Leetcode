# 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False
        if len(nums) <= k:
            return len(nums) > len(set(nums))
        part = set(nums[0:k + 1])
        if len(part) != k + 1:
            return True
        for i in range(1, len(nums) - k):
            part.remove(nums[i - 1])
            part.add(nums[k + i])
            if len(part) != k + 1:
                return True
        return False
        
