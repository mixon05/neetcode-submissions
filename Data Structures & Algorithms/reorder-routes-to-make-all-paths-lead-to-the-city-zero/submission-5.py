class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for start, end in connections:
            adj[start].append((end, True))
            adj[end].append((start, False))
        visited = set()
        queue = deque()
        visited.add(0)
        queue.append(0)

        result = 0
        while queue:
            node = queue.popleft()
            for nei, nei_dir in adj[node]:
                if nei in visited:
                    continue
                if nei_dir:
                    result += 1
                queue.append(nei)
                visited.add(nei)
                        
        return result