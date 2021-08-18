# 270. Closest Binary Search Tree Value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:  
            cur = root.val
            
            while root:
                if abs(root.val - target) < abs(cur - target):
                    cur = root.val
                else:
                    if root.val < target:
                        root = root.right
                    else:
                        root = root.left
                        
            return cur
        
# Reference
# https://leetcode.com/problems/closest-binary-search-tree-value/discuss/344282/Python3-Closest-Binary-Search-Tree-Value