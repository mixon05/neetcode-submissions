from collections import defaultdict

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
        
        visited = set()

        def dfs(bomb):
            if bomb in visited:
                return 0
            
            count = 1
            visited.add(bomb)
            for nei in adj[bomb]:
                count += dfs(nei)

            return count
        
        max_bombs = 0
        for i in range(n):
            max_bombs = max(max_bombs, dfs(i))
            visited.clear()
        return max_bombs

