class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = 0
        res = 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                min_idx = i
            res +=  i - min_idx + 1
        return res