class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dict()
        def dfs(str_left):
            if str_left in dp:
                return dp[str_left]
            if not str_left:
                return 1
            if str_left[0] == "0":
                return 0
            n = len(str_left)
            if n == 1:
                return 1
            result = dfs(str_left[1:])
            if 10 <= int(str_left[0:2]) <= 26:
                result += dfs(str_left[2:])
            dp[str_left] = result
            return result
        return dfs(s)