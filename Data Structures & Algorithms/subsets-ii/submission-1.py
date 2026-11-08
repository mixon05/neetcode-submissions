class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        def dfs(curr_arr, i):
            for j in range(i, len(nums)):
                if j > i and nums[j - 1] == nums[j]:
                    continue
                curr_arr.append(nums[j])
                result.append(curr_arr.copy())
                dfs(curr_arr, j + 1)
                curr_arr.pop()
        dfs([], 0)
        return result