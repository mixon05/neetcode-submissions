class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image

        ROWS, COLS = len(image), len(image[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r: int, c: int) -> None:
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or image[sr][sc] != image[r][c]:
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

            image[r][c] = color

        dfs(sr, sc)

        return image