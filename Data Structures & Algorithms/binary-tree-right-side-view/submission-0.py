# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([(root, 0)])
        res = []
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue
            if len(res) <= depth:
                res.append(node.val)
            queue.append((node.right, depth + 1))
            queue.append((node.left, depth + 1))
        return res