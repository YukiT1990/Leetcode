# 1013. Partition Array Into Three Parts With Equal Sum

# Reference
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/discuss/352417/Solution-in-Python-3-(beats-~99)-(With-Detailed-Explanation)-(-O(n)-time-)-(-O(1)-space-)

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_array = sum(arr)
        if sum_array % 3 != 0:
            return False
        g, C, p = sum_array // 3, 0, 0
        for a in arr[:-1]:
            C += a
            if C == g:
                if p == 1:
                    return True
                C, p = 0, 1
        return False