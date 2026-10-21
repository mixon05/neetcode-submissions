class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1:
                    is_sub_island = True
                    queue = deque([(r, c)])
                    grid2[r][c] = 0
                    if grid1[r][c] == 0:
                        is_sub_island = False
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid2[nr][nc] == 1:
                                queue.append((nr, nc))
                                grid2[nr][nc] = 0
                                if grid1[nr][nc] == 0:
                                    is_sub_island = False
                    count += is_sub_island
        return count