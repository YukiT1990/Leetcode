# 226. Invert Binary Tree

# Reference
# https://leetcode.com/problems/invert-binary-tree/discuss/664132/Python-O(n)-by-DFS-BFS-w-Visualization-90%2B

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            
            if root.left:
                self.invertTree(root.left)
                
            if root.right:
                self.invertTree(root.right)
                
            return root
        
        else:
            return None