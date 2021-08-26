# 572. Subtree of Another Tree

# Reference
# https://leetcode.com/problems/subtree-of-another-tree/discuss/386209/Python-98-speed-with-comments

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def traverse_tree(s):
            if s:
                return f"#{s.val} {traverse_tree(s.left)} {traverse_tree(s.right)}"
            return None
        
        string_s = traverse_tree(root)
        string_t = traverse_tree(subRoot)
        # print(string_s)
        # print(string_t)
        if string_t in string_s:
            return True
        return False
    
        
            
