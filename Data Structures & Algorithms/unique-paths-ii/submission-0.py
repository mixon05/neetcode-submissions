class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * COLS
        dp[-1] = 1
        for r in range(ROWS - 1, -1, -1):
            dp[-1] = 0 if obstacleGrid[r][-1] else dp[-1]
            for c in range(COLS - 2, -1, -1):
                dp[c] = 0 if obstacleGrid[r][c] else  dp[c] + dp[c+1]
        return dp[0]