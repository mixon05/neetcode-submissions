# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d_max = 0
        def dfs(node):
            nonlocal d_max
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            d_max = max(d_max, left + right)
            return 1 + max(left, right)
        dfs(root)
        return d_max