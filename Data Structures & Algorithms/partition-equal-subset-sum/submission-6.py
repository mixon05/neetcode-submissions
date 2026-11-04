class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum = sum(nums)
        if list_sum % 2 != 0:
            return False
        half_sum = int(list_sum / 2)
        dp = [[0] * len(nums) for _ in range(half_sum)]
        def dfs(rest, i):
            if rest == 0:
                return True
            if dp[rest - 1][i - 1]:
                return False
            for j in range(i, len(nums)):
                diff = rest - nums[j]
                if diff < 0:
                    continue
                if dfs(diff, j + 1):
                    return True
            dp[rest - 1][i - 1] = 1
            return False
        return dfs(half_sum, 0)