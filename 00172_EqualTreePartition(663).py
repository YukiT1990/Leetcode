# 663. Equal Tree Partition
# tree value sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sums_array = []
        def helper(node: Optional[TreeNode]):
            nonlocal sums_array
            if not node:
                return 0
            else:
                left_sum = helper(node.left)
                right_sum = helper(node.right)
                if node.left:
                    sums_array.append(left_sum)
                if node.right:
                    sums_array.append(right_sum)
                return left_sum + node.val + right_sum
        total_sum = helper(root)
        # print(total_sum)
        # print(sums_array)
        for value in sums_array:
            if total_sum - value == value:
                return True
        return False
                