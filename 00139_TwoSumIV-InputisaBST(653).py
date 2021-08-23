# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 148 ms	20.5 MB
        values = []
        def collect_values(root: Optional[TreeNode], values):
            if root:
                values.append(root.val)
            if root.left:
                collect_values(root.left, values)
            if root.right:
                collect_values(root.right, values)
            
        collect_values(root, values)
        # print(values)
        if len(values) < 2:
            return False
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if k - values[i] == values[j]:
                    return True
        return False
    
        # 72 ms	16.3 MB	
        # Reference
        # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/354042/Python3-Breadth-First-Search-and-Inorder-Travesal
        # if not root:
        #     return False
        # queue, seen = deque([root]),set()
        # while queue:
        #     cur = queue.popleft()
        #     if cur.val in seen:
        #         return True
        #     else:
        #         seen.add(k-cur.val)
        #         if cur.left: queue.append(cur.left)
        #         if cur.right: queue.append(cur.right)
        # return False