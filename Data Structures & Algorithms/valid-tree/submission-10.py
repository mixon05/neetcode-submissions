class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        nodes = defaultdict(list)
        for start, end in edges:
                nodes[start].append(end)
                nodes[end].append(start)
        if len(nodes) == 0:
            return False
        queue = deque()
        visited = set()
        first = next(iter(nodes))
        queue.append((None, first))
        visited.add(first)

        while queue:
            prev, node = queue.popleft()
            for neighbor in nodes[node]:
                if neighbor in visited:
                    if prev == neighbor:
                        continue
                    return False
                queue.append((node, neighbor))
                visited.add(neighbor)
        return len(visited) == n