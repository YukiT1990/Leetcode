# 671. Second Minimum Node In a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = []
        def helper(root: Optional[TreeNode]):
            nonlocal values
            if root:
                if root.val not in values:
                    values.append(root.val)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
                    
        helper(root)
        # print(values)
        values.sort()
        # print(values)
        if len(values) < 2:
            return -1
        else:
            return values[1]