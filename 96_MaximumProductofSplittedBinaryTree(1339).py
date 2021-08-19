# 1339. Maximum Product of Splitted Binary Tree

# Reference
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/496601/Python-3-(DFS)-(beats-100)-(nine-lines)

# Modulo 10^9+7 (1000000007)
# https://www.geeksforgeeks.org/modulo-1097-1000000007/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums, M = [], 10 ** 9 + 7
        
        def SumTree(root: Optional[TreeNode]):
            if not root:
                return 0
            sums.append(root.val + SumTree(root.left) + SumTree(root.right))
            return sums[-1]
        
        SumTree(root)
        S, _ = sums[-1], sums.sort()
        for i, s in enumerate(sums):
            if s >= S//2:
                return max(sums[i - 1] * (S-sums[i - 1]), sums[i] * (S - sums[i])) % M
        