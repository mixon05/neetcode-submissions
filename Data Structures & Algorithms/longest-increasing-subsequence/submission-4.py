class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            max_sequence = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_sequence = max(max_sequence, dp[j] + 1)
            dp[i] = max_sequence
        return max(dp)