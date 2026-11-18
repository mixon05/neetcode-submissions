class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        min_idx = 0
        prev_count = 1
        curr_count = 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                min_idx = i
            curr_count = prev_count + i - min_idx + 1
            prev_count = curr_count
        return curr_count