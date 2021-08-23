# 501. Find Mode in Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        values = {}
        def collect_values(root: Optional[TreeNode], values):
            if root:
                values[root.val] = values.get(root.val, 0) + 1
            if root.left:
                collect_values(root.left, values)
            if root.right:
                collect_values(root.right, values)
            
        collect_values(root, values)
        # print(values)
        max_value = max(values.values())
        # result = []
        # for k, v in values.items():
        #     if v == max_value:
        #         result.append(k)
        # return result
        return [k for k,v in values.items() if v == max_value]
        

        