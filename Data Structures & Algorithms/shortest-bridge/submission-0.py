class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        first_one = None
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    first_one = (r, c)
                    break
            if first_one:
                break
        
        visit = set()
        visit.add(first_one)
        queue = deque()
        queue.append(first_one)

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                queue.append((nr, nc))

        for r, c in visit:
            queue.append((r, c, 0))
        while queue:
            r, c, d = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit:
                    continue
                if grid[nr][nc] == 1:
                    return d
                queue.append((nr, nc, d + 1))
                visit.add((nr, nc))