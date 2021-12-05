# 337. House Robber III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 44 ms	16.3 MB
        # https://leetcode.com/problems/house-robber-iii/discuss/872676/Python-3-or-DFS-Backtracking-or-Explanation
        def dfs(node):
            if not node:
                return 0, 0
            left, right = dfs(node.left), dfs(node.right)
            v_take = node.val + left[1] + right[1]
            v_not_take = max(left) + max(right)
            return v_take, v_not_take
        return max(dfs(root))

        # 44 ms	16.3 MB
        # https://leetcode.com/problems/house-robber-iii/discuss/872676/Python-3-or-DFS-Backtracking-or-Explanation
        def dfs(node):
            return (node.val + (left := dfs(node.left))[1] + (right := dfs(node.right))[1], max(left) + max(right)) if node else (0, 0)
        return max(dfs(root))

        # 60 ms	18.7 MB
        # https://leetcode.com/problems/house-robber-iii/discuss/946573/Python-3-Explained-Solution-(video-%2B-code)
        @lru_cache(None)
        def helper(node, parent_stolen):
            if not node:
                return 0

            if parent_stolen:
                # we did steal from parent
                # the only option is to not steal since we stole from the parent
                return helper(node.left, False) + helper(node.right, False)

            else:
                # we did NOT steal parent
                # Given a choice to choose b/w stealing or not stealing
                # stealing at the current node
                steal = node.val + \
                    helper(node.left, True) + helper(node.right, True)

                # NOT stealing current node
                not_stealing = helper(node.left, False) + \
                    helper(node.right, False)

                return max(steal, not_stealing)

        return helper(root, False)
