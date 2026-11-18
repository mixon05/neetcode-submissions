class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        min_idx = 0
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                min_idx = i
            dp[i] = dp[i - 1] + i - min_idx + 1
        return dp[-1]