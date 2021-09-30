# 698. Partition to K Equal Sum Subsets

# Reference
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/867956/Python3-Two-solutions-DP-with-Bit-mask(48ms)-DFS%2Bbacktracking-with-detailed-explanations

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N < k or sum(nums) / k != sum(nums) // k:
            return False
        nums = sorted(nums, reverse=True)
        
        def dp(mask, cur, memo):
            if mask == 0:
                return cur == 0
            elif cur == 0:
                return dp(mask, sum(nums) / k, memo)
            if (mask, cur) not in memo:
                res = False
                for bit in range(N):
                    if mask & (1 << bit):
                        if nums[bit] > cur:
                            continue
                        if dp(mask ^ (1 << bit), cur-nums[bit], memo):
                            res = True
                            break
                memo[(mask, cur)] = res
            return memo[(mask, cur)]
        
        return dp(2 ** N-1, sum(nums) / k, dict())