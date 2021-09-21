# 965. Univalued Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # 32 ms	14.4 MB
        is_uni_valued = True
        def dfs(root: Optional[TreeNode]):
            nonlocal is_uni_valued
            if root:
                if root.left:
                    if root.val != root.left.val:
                        is_uni_valued = False
                        return
                    dfs(root.left)
                if root.right:
                    if root.val != root.right.val:
                        is_uni_valued = False
                        return
                    dfs(root.right)
                    
        dfs(root)
        return is_uni_valued
    
        # 32 ms	14.1 MB
        # Reference
        # https://leetcode.com/problems/univalued-binary-tree/discuss/440997/Accepted-Python-Answer%3A-Easy-to-Understand
        # if not root:
        #     return True
        
        # if root.left and root.val != root.left.val:
        #     return False
            
        # if root.right and root.val != root.right.val:
        #     return False
        
        # return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)