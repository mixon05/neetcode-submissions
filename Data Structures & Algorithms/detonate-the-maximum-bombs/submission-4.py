from collections import defaultdict, deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = defaultdict(list)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                if (x1-x2)**2 + (y1-y2)**2 <= r1**2:
                    adj[i].append(j)
        

        max_bombs = 0
        for i in range(n):
            result = 0
            queue = deque()
            visited = set()
            queue.append(i)
            visited.add(i)

            while queue:
                bomb = queue.popleft()
                result += 1

                for nei in adj[bomb]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    queue.append(nei)
                    
            max_bombs = max(max_bombs, result)

        return max_bombs

