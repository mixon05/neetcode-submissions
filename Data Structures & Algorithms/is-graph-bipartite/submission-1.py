from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)

        for i, v in enumerate(visited):
            if v: 
                continue
            queue = deque()
            queue.append((i, 1))

            while queue:
                node, color = queue.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == color:
                        return False
                    elif visited[neighbor] == -color:
                        continue
                    queue.append((neighbor, -color))
                    visited[neighbor] = -color
        
        return True