# 404. Sum of Left Leaves

# Reference
# https://leetcode.com/problems/sum-of-left-leaves/discuss/808981/Python-DFS-Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, isleft):
            if not node:
                return 0
            
            if not node.left and not node.right and isleft:
                return node.val
            
            return dfs(node.left, True) +  dfs(node.right, False)
        
        return dfs(root, False)