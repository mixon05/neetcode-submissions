"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(old_node):
            if old_node in old_to_new:
                return old_to_new[old_node]
            
            new_node = Node(old_node.val)
            old_to_new[old_node] = new_node

            new_n = []
            for n in old_node.neighbors:
                new_n.append(dfs(n))
            
            new_node.neighbors = new_n

            return new_node

        return dfs(node) if node else None

        