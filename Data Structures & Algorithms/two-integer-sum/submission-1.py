class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = {}
        for i in range(len(nums)):
            if nums[i] in left:
                return [left[nums[i]], i]
            left[target - nums[i]] = i