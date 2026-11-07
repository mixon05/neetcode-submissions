class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        n = len(nums)
        def dfs(curr_arr, i):
            if i == n:
                return
            for j in range(i, n):
                new_arr = curr_arr.copy()
                new_arr.append(nums[j])
                result.append(new_arr)
                dfs(new_arr, j + 1)
            return
        dfs([], 0)
        return result
            