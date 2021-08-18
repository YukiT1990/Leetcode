# 235. Lowest Common Ancestor of a Binary Search Tree

# Reference
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/693896/Python-Explained.-Simple-Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur_value = root.val
        if p.val > cur_value and q.val > cur_value:
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif p.val < cur_value and q.val < cur_value:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else:
            return root
        
## APPROACH : RECURSION ##
        ## LOGIC ##
        # Both p and q are smaller than current node, then search left-subtree by recursive
        # Both p and q are larger than current node, then search right-subtree by recursive
        # Both p and q are not on the same side of current node, then current node must be the Lowest common ancestor of ( p, q )
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##