import sys
sys.setrecursionlimit(10003)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node] = False
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            visited[node] = True
            return True
        
        return [i for i in range(len(graph)) if dfs(i)]