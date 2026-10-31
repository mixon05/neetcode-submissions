class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        max_product = nums[0]
        for i in range(1, len(nums)):
            prev_max_cp = prev_max
            prev_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            prev_min = min(nums[i], prev_min * nums[i], prev_max_cp * nums[i])
            max_product = max(max_product, prev_max)
        return max_product