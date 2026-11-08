class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        subset = []
        def dfs(i):
            for j in range(i, len(nums)):
                subset.append(nums[j])
                result.append(subset.copy())
                dfs(j + 1)
                subset.pop()
            return
        dfs(0)
        return result
