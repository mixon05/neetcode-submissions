class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = dict()
        def dfs(amount_left):
            if amount_left == 0:
                return 0
            if amount_left in dp:
                return dp[amount_left]
            min_count = float("inf")
            for coin in coins:
                if amount_left - coin >= 0:
                    min_count = min(min_count, 1 + dfs(amount_left - coin))
            dp[amount_left] = min_count
            return min_count
        return -1 if dfs(amount) == float("inf") else dfs(amount)