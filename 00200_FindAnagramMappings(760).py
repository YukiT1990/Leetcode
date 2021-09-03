# 760. Find Anagram Mappings

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            result.append(nums2.index(num))
        return result