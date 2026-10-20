class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            total = grid[r][c]
            for dr, dc in directions:
                total += dfs(r+dr, c+dc)

            return total


        max_fish_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0 and (r, c) not in visited:
                    max_fish_count = max(max_fish_count, dfs(r, c))

        return max_fish_count

