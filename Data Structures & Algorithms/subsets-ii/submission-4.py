class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        subset = []
        def dfs(i):
            for j in range(i, len(nums)):
                if j > i and nums[j - 1] == nums[j]:
                    continue
                subset.append(nums[j])
                result.append(subset.copy())
                dfs(j + 1)
                subset.pop()
        dfs(0)
        return result