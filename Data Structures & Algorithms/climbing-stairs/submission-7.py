class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2, 3: 3}

        def dfs(k):
            if k in cache:
                return cache[k]
            cache[k] = dfs(k - 1) + dfs(k - 2)
            return cache[k]

        return dfs(n)
        