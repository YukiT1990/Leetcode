# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # exist = set()
        # for num in nums:
        #     if num in exist:
        #         return True
        #     else:
        #         exist.add(num)
        # return False

    # improved
        exist = set(nums)
        if len(nums) > len(exist):
            return True
        else:
            return False
            
