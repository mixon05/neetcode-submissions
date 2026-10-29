class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] == "X":
                return
            visited.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if (r, c) not in visited:
                    board[r][c] = "X"
            