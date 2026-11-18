class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[None] * i for i in range(1, len(triangle) + 1)]
        def dfs(r, i):
            if i >= len(triangle[r]):
                return float("inf")
            if r == len(triangle) - 1:
                return triangle[r][i]
            if dp[r][i] != None:
                return dp[r][i]
            
            s = triangle[r][i]

            left = dfs(r + 1, i)
            right = dfs(r + 1, i + 1)
            dp[r][i] = min(s + left, s + right)
            return dp[r][i]

        return dfs(0, 0)