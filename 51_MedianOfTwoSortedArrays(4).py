# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        length = m + n
        array = []

        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                array.append(nums1[i])
                i += 1
            else:
                array.append(nums2[j])
                j += 1

        if i < m:
            array = array + nums1[i:]
        if j < n:
            array = array + nums2[j:]

        if length % 2 == 0:
            return (array[length // 2 - 1] + array[length // 2]) / 2.0
        else:
            return array[length // 2]
