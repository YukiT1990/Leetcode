# 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #         values = []
        #         def dfs(root: Optional[TreeNode]):
        #             nonlocal values
        #             if root:
        #                 values.append(root.val)
        #             if root.left:
        #                 dfs(root.left)
        #             if root.right:
        #                 dfs(root.right)

        #         dfs(root)
        #         values.sort()
        #         result = 0
        #         for val in values:
        #             if val >= low and val <= high:
        #                 result += val
        #         return result

        # Reference
        # https://leetcode.com/problems/range-sum-of-bst/discuss/1213314/Python-3-Faster-than-99.54-Simple-Solution

        if root:
            if root.val < low:
                return self.rangeSumBST(root.right, low, high)
            elif root.val > high:
                return self.rangeSumBST(root.left, low, high)
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        else:
            return 0
