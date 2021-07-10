# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right) and root.val != targetSum:
            return False
        if not (root.left or root.right) and root.val == targetSum:
            return True
        else:
            targetSum -= root.val
            # if the tree has at least a root-to-leaf path such that adding up all the values along the path equals targetSum
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
