class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * m
        for _ in range(n - 2, -1, -1):
            for i in range(m - 2, -1, -1):
                row[i] = row[i] + row[i + 1]
        return row[0]