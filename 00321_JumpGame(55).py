# 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 4398 ms	15.3 MB
        # dp = [False for _ in range(len(nums))]
        # dp[0] = True
        # # print(dp)
        # for i in range(1, len(nums)):
        #     for j in range(i-1, -1, -1):
        #         if dp[i] == True:
        #             break
        #         if dp[j] == True and j + nums[j] >= i:
        #             dp[i] = True
        # return dp[-1]
    
    
        # 889 ms	15.3 MB
        # Reference
        # https://leetcode.com/problems/jump-game/discuss/1233260/Easy-python-Solution
        j=0
        for i in range(len(nums)):
            if i>j:
                return False
            j=max(j,i+nums[i])
        return True