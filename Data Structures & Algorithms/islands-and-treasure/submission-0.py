class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
        
        while queue:
            r, c, d = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = d + 1
                queue.append((nr, nc, d + 1))
