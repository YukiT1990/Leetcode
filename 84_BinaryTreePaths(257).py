# 257. Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        first_temp_str = str(root.val)
        
        def helper(root: Optional[TreeNode], temp_str):
            new_str = "->" + str(root.val)
            temp_str += new_str
            if root.left:
                helper(root.left, temp_str)
            if root.right:
                helper(root.right, temp_str)
            if not root.left and not root.right:
                result.append(temp_str)
        
        
        if root.left:
            helper(root.left, first_temp_str)
        if root.right:
            helper(root.right, first_temp_str)
        if not root.left and not root.right:
            result.append(first_temp_str)
                
        return result