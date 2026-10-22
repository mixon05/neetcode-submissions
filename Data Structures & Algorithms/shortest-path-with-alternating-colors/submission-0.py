class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_nodes = defaultdict(list)
        blue_nodes = defaultdict(list)
        for start, end in redEdges:
            red_nodes[start].append(end)
        for start, end in blueEdges:
            blue_nodes[start].append(end)

        visited = set()
        queue = deque()
        output = [-1] * n
        output[0] = 0
        visited.add((0, 'r'))
        visited.add((0, 'b'))
        queue.append((0, 'r', 0))
        queue.append((0, 'b', 0))

        while queue:
            node, color, distance = queue.popleft()

            if output[node] == -1:
                output[node] = distance

            if color == 'r':
                for neighbor in blue_nodes[node]:
                    if (neighbor, 'b') in visited:
                        continue
                    visited.add((neighbor, 'b'))
                    queue.append((neighbor, 'b', distance + 1))
            if color == 'b':
                for neighbor in red_nodes[node]:
                    if (neighbor, 'r') in visited:
                        continue
                    visited.add((neighbor, 'r'))
                    queue.append((neighbor, 'r', distance + 1))

        return output


