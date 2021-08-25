# 543. Diameter of Binary Tree

# Reference
# https://leetcode.com/problems/diameter-of-binary-tree/discuss/637354/Easy-Python-solution-with-details-from-O(n2)-to-O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        diameter, height = self.getDiameterAndHeight(root)
        return diameter
        
    
    def getDiameterAndHeight(self, node):
        if not node:
            return 0, 0            
        ldiameter, lheight = self.getDiameterAndHeight(node.left)
        rdiameter, rheight = self.getDiameterAndHeight(node.right)
        
        # Compute the height of the current node
        height = 1 + max(lheight, rheight)
		
        # The diameter is the max between lheight + rheight , ldiameter and rdiamter
        diameter = max(lheight + rheight, ldiameter, rdiameter)
        return diameter, height