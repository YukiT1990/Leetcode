# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # make the middle value to be the root
        left = 0
        right = len(nums) - 1
        mid = (left+right) // 2
        if mid < 0:
            return

        root = TreeNode(nums[mid])

        # first half array to be the left part of the tree
        root.left = self.sortedArrayToBST(nums[:mid])

        # second half array to be the right part of the tree
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
