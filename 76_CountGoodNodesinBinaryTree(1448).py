# 1448. Count Good Nodes in Binary Tree

# Reference
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/1218157/Python-3%3A-DFS-with-a-detailed-explanation-suitable-for-novice-users

# DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        if root and not root.left and not root.right: return 1
        
        result = 0
        
        def _helper(node, max_val):
            nonlocal result
            if not node: return
            if node.val >= max_val:
                result += 1
            max_val = max(max_val, node.val)
            if node.left:
                _helper(node.left, max_val)
            if node.right:
                _helper(node.right, max_val)
                
        _helper(root, root.val)
        
        return result