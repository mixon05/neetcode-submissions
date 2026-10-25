import sys
sys.setrecursionlimit(10200)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node] == 2

            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            visited[node] = 2
            return True
        
        return [i for i in range(len(graph)) if dfs(i)]