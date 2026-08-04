class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        totalMaxArea = 0
        currentMaxArea = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c):
            nonlocal currentMaxArea
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return

            currentMaxArea += 1
            visited.add((r, c))

            for (dr, dc) in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    dfs(r, c)
                    totalMaxArea = max(totalMaxArea, currentMaxArea)
                    currentMaxArea = 0


        return totalMaxArea