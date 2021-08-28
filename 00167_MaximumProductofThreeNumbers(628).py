# 628. Maximum Product of Three Numbers

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 417 ms	15.4 MB
        nums = sorted(nums, reverse=True)
        return max(nums[0] * nums[1] * nums[2], nums[len(nums) - 1] * nums[len(nums) - 2] * nums[0])
    
        # 252 ms	15.5 MB
        # Reference
        # https://leetcode.com/problems/maximum-product-of-three-numbers/discuss/734686/Python-O(n)-time-O(1)-space
        # smallestTwo = [float('inf')]*2
        # largestThree = [float('-inf')]*3
        # for num in nums:
        #     if num <= smallestTwo[0]:
        #         smallestTwo[0] = num
        #         smallestTwo.sort(reverse=True)
        #     if num >= largestThree[0]:
        #         largestThree[0] = num
        #         largestThree.sort()
        # return max(smallestTwo[0]*smallestTwo[1]*largestThree[2], 
        #            largestThree[0]*largestThree[1]*largestThree[2])
        