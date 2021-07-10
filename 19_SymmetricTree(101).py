# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def checkSymmetry(left_node, right_node):

            if not left_node and not right_node:
                return True

            elif not left_node and right_node:
                return False

            elif left_node and not right_node:
                return False
            else:
                if left_node.val == right_node.val:
                    return checkSymmetry(left_node.left, right_node.right) and checkSymmetry(left_node.right, right_node.left)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return checkSymmetry(root.left, root.right)
