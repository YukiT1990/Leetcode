# 325. Maximum Size Subarray Sum Equals k

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Time Limit Exceeded
        # result = [0 for i in range(len(nums))]
        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(i, len(nums)):
        #         temp += nums[j]
        #         if temp == k:
        #             result[i] = j - i + 1
        # return max(result)
    
    
        # Reference
        # https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/256463/Optimal-Easy-to-Understand-O(n)-beats-94-Python-Code
        seen_sum = {0:0}
        total_sum, largest_len = 0, 0
        for i in range(len(nums)):
            total_sum += nums[i]
            if total_sum == k:
                largest_len = i + 1
            else: 
                required = total_sum - k
                if required in seen_sum:
                    largest_len = max(largest_len, i - seen_sum[required])
            if total_sum not in seen_sum:
                seen_sum[total_sum] = i
        return largest_len