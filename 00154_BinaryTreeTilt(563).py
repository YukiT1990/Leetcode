# 563. Binary Tree Tilt

# get the sum of values of tree
# tree sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
          # 564 ms	29.7 MB
#         if not root:
#             return 0
        
#         def collect_values(root: Optional[TreeNode], values):
#             if not root:
#                 return
#             if root:
#                 values.append(root.val)
#             if root.left:
#                 collect_values(root.left, values)
#             if root.right:
#                 collect_values(root.right, values)
            
        
#         sum_tilt = 0
        
#         def tiltify(root: Optional[TreeNode]):
#             nonlocal sum_tilt
#             left_val, right_val = 0, 0
#             if root.left:
#                 valuesL = []
#                 collect_values(root.left, valuesL)
#                 left_val = sum(valuesL)
#             if root.right:
#                 valuesR = []
#                 collect_values(root.right, valuesR)
#                 right_val = sum(valuesR)
#             tilt = abs(left_val - right_val)
#             sum_tilt += tilt
#             if root.left:
#                 tiltify(root.left)
#             if root.right:
#                 tiltify(root.right)
                
#         tiltify(root)
        
#         return sum_tilt
    
        # 52 ms	16.3 MB
        # Reference
        # https://leetcode.com/problems/binary-tree-tilt/discuss/520397/Python-O(n)-by-DFS.-90%2B-with-Hint-and-Comment
    
        tilt_sum = 0
        
        def helper( node: TreeNode):
            
            if not node:
				# base case: empty node or empty tree
                return 0
            
            else:
                
                left_sum = helper(node.left)
                right_sum = helper(node.right)
                
				# update tilt sum for whloe binary tree
                nonlocal tilt_sum
                tilt_sum += abs(left_sum - right_sum)
				
                return left_sum + node.val + right_sum
        
        # ---------------------------------------------
        
        helper( root )
        return tilt_sum