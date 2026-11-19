class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or grid[r][c] == 0:
                return 0
            gold = grid[r][c]
            grid[r][c] = -1
            max_gold = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                max_gold = max(max_gold, dfs(nr, nc))
            grid[r][c] = gold
            return gold + max_gold
        max_gold = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_gold = max(max_gold, dfs(r, c))
        return max_gold