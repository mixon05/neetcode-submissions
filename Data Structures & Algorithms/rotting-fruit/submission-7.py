class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        freshCount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        if not freshCount:
            return 0

        minutes = 0

        while queue:
            for _ in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                            continue

                        freshCount -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            
            minutes += 1

        return -1 if freshCount else minutes - 1