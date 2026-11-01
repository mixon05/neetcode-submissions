class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        nums_cp1 = nums[0:-1]
        nums_cp2 = nums[1:]
        def rob_helper(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]
        return max(rob_helper(nums_cp1), rob_helper(nums_cp2))