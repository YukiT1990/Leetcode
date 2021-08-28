# 606. Construct String from Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        def traverse(root: Optional[TreeNode]):
            nonlocal result
            result += str(root.val)
            if root.left or root.right:
                if root.left:
                    result += '('
                    traverse(root.left)
                    result += ')'
                if root.right:
                    if not root.left:
                        result += '()'
                    result += '('
                    traverse(root.right)
                    result += ')'
                
        traverse(root)
        return result