# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root1, root2, result: []) -> []:
        if root1 and root2:
            inorder(root1.left, root2.left, result)
            result.append(root1.val == root2.val)
            inorder(root1.right, root2.right, result)
        elif (root1 and not(root2)) or (not(root1) and root2):
            result.append(False)
        return result

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        result = []
        array = inorder(p, q, result)
        if False in array:
            return False
        else:
            return True
