# 1120. Maximum Average Subtree

# Reference
# https://leetcode.com/problems/maximum-average-subtree/discuss/338427/Simple-Python-solution-100-faster

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = 0
        
        def traverse(node):
            if node is None:
                return [0, 0]
            
            lsum, lcount = traverse(node.left)
            rsum, rcount = traverse(node.right)
            
            self.max_avg = max(self.max_avg, (lsum + rsum + node.val) / (lcount + rcount + 1))
            
            return [lsum + rsum + node.val, lcount + rcount + 1]
        
        traverse(root)
        return self.max_avg