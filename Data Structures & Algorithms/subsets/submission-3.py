class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        n = len(nums)
        def dfs(curr_arr, i):
            for j in range(i, n):
                curr_arr.append(nums[j])
                result.append(curr_arr.copy())
                dfs(curr_arr, j + 1)
                curr_arr.pop()
            return
        dfs([], 0)
        return result
