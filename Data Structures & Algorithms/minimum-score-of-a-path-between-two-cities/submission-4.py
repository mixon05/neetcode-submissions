class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for start, end, dist in roads:
            adj[start].append((end, dist))
            adj[end].append((start, dist))
        
        min_global = float("inf")
        visited = set()
        visited.add(1)
        queue = deque()
        queue.append(1)

        while queue:
            city = queue.popleft()
            for nei, nei_score in adj[city]:
                if nei not in visited:
                    queue.append(nei)
                min_global = min(min_global, nei_score)
                visited.add(nei)
                

        return min_global
