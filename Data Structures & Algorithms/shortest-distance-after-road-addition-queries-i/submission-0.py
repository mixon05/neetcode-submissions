class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        nodes = defaultdict(list)
        for i in range(n-1):
            nodes[i].append(i+1)
        
        result = []

        for start, end in queries:
            nodes[start].append(end)

            queue = deque()
            queue.append((0, 0))
            
            visited = set()
            visited.add(0)

            while queue:
                node, dist = queue.popleft()
                for neighbor in nodes[node]:
                    if neighbor in visited:
                        continue
                    if neighbor == n - 1:
                        result.append(dist + 1)
                    queue.append((neighbor, dist + 1))
                    visited.add(neighbor)
        return result

