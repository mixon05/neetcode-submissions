class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [1, 1], [-1, 1], [0, 1], [0, -1], [-1, -1], [1, -1]]
        visited = set()
        queue = deque()
        visited.add((0, 0))
        queue.append((0, 0))

        length = 1

        shortest_path = math.sqrt(ROWS**2 + COLS**2)

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for [dr, dc] in directions:
                    new_r, new_c = r + dr, c + dc
                    if min(new_r, new_c) < 0 or new_r >= ROWS or new_c >= COLS or (new_r, new_c) in visited or grid[r][c] == 1:
                        continue

                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
                   
            length += 1
        
        return -1
            