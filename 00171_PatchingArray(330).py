# 330. Patching Array

# Reference
# https://leetcode.com/problems/patching-array/discuss/1196758/Python3-greedy

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = prefix = k = 0
        while prefix < n:
            if k < len(nums) and nums[k] <= prefix + 1:
                prefix +=nums[k]
                k += 1
            else:
                ans += 1
                prefix += prefix + 1
            # print("ans")
            # print(ans)
            # print("prefix")
            # print(prefix)
            # print("k")
            # print(k)
        return ans