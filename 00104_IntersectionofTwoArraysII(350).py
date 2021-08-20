# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        # return [x for x in nums1 if x in nums2]
        for x in nums1:
            if x in nums2:
                result.append(x)
                # If the list contains more than one matching the specified value, only the first one is deleted.
                nums2.remove(x)
        return result