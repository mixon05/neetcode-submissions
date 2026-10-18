class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 1 or (x, y) in visited:
                return 0
            if x == ROWS -1 and y == COLS - 1 and grid[x][y] == 0:
                return 1

            visited.add((x, y))

            count = 0
            for dx, dy in directions:
                count += dfs(x + dx, y + dy)
            
            visited.remove((x, y))
            return count

        return dfs(0, 0)
        