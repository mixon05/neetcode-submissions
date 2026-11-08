# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, sub_node):
            if not node and not sub_node:
                return True
            if not node or not sub_node or node.val != sub_node.val:
                return False
            return dfs(node.left, sub_node.left) and dfs(node.right, sub_node.right)
                
        queue = deque([root])
        starts = []
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if node.val == subRoot.val:
                starts.append(node)
            queue.append(node.left)
            queue.append(node.right)
        for node in starts:
            if dfs(node, subRoot):
                return True
        return False