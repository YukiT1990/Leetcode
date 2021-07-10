# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(root):
        if(root == None):
            return 0
        return max(height(root.left), height(root.right)) + 1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if(root == None):
            return True
        if(self.isBalanced(root.left) == False):
            return False
        if(self.isBalanced(root.right) == False):
            return False
        lh = height(root.left)
        rh = height(root.right)
        if(abs(lh-rh) > 1):
            return False
        else:
            return True
