# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 76 ms	14.6 MB
        result = []
        for num1 in nums1:
            index = nums2.index(num1)
            for num2 in nums2[index:]:
                if num2 > num1:
                    result.append(num2)
                    break
                if num2 == nums2[-1]:
                    result.append(-1)
        return result
    
        # 40 ms	14.4 MB
        # Reference
        # https://leetcode.com/problems/next-greater-element-i/discuss/824654/Python-3-greater-94.64-faster.-Used-stack-and-dictionary.-Explanation-added
        
        # if not nums2:
        #     return None

        # mapping = {}
        # result = []
        # stack = []
        # stack.append(nums2[0])

        # for i in range(1, len(nums2)):
        #     while stack and nums2[i] > stack[-1]:       # if stack is not empty, then compare it's last element with nums2[i]
        #         mapping[stack[-1]] = nums2[i]           # if the new element is greater than stack's top element, then add this to dictionary 
        #         stack.pop()                             # since we found a pair for the top element, remove it.
        #     stack.append(nums2[i])                      # add the element nums2[i] to the stack because we need to find a number greater than this

        # for element in stack:                           # if there are elements in the stack for which we didn't find a greater number, map them to -1
        #     mapping[element] = -1

        # for i in range(len(nums1)):
        #     result.append(mapping[nums1[i]])
        # return result