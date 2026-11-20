class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr_row = [1] * m
        for _ in range(n - 2, -1, -1):
            for i in range(m - 2, -1, -1):
                curr_row[i] = curr_row[i] + curr_row[i + 1]
        return curr_row[0]