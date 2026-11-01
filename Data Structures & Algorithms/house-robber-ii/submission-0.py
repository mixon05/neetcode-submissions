class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums_cp1 = nums[0:-1]
        nums_cp2 = nums[1:]
        return max(self.rob_helper(nums_cp1), self.rob_helper(nums_cp2))

    def rob_helper(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]