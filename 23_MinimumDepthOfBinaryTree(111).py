# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def calcMinDepth(node, hight, minimum):

        if hight > minimum:
            return minimum

        if not node:
            return float('inf')

        if (not node.left) and (not node.right):
            minimum = min(minimum, hight)
            return minimum
        # when there is at least one child
        return min(calcMinDepth(node.left, hight + 1, minimum), calcMinDepth(node.right, hight + 1, minimum))

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if (not root.left) and (not root.right):
            return 1

        hight = 1
        minimum = float('inf')

        return calcMinDepth(root, hight, minimum)
