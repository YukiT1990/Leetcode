# 1018. Binary Prefix Divisible By 5

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # 928 ms	17.2 MB
        result = []
        nums = list(map(str, nums))
        binary = ''
        for i in range(len(nums)):
            binary += nums[i]
            # print(binary)
            result.append(int(binary, 2) % 5 == 0)
        return result


        # 316 ms	15 MB
        # Reference
        # https://leetcode.com/problems/binary-prefix-divisible-by-5/discuss/505181/Python3-using-yield
        # x = 0
        # for i in range(len(nums)):
        #     x = x*2+nums[i]
        #     yield x%5==0