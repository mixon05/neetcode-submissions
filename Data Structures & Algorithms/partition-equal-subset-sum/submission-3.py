class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum = sum(nums)
        if list_sum % 2 != 0:
            return False
        def dfs(rest, i):
            if rest == 0:
                return True
            for j in range(i, len(nums)):
                if dfs(rest - nums[j], j + 1):
                    return True
            return False
        return dfs(list_sum / 2, 0)