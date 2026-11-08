class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        def dfs(r, c, i ):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r, c) in visited:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r, c))
            for dr, dc in dirs:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            visited.remove((r, c))
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
