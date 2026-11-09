# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from dataclasses import dataclass

@dataclass
class Boundary:
    left: int
    right: int

    def within(self, value):
        return self.left < value < self.right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, bounds):
            if not node:
                return True
            if not bounds.within(node.val):
                return False
            left = dfs(node.left, Boundary(bounds.left, node.val))
            right = dfs(node.right, Boundary(node.val, bounds.right))
            return left and right
        return dfs(root.left, Boundary(float("-inf"), root.val)) and dfs(root.right, Boundary(root.val, float("inf")))