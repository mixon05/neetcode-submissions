class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def dfs(curr_arr, i):
            for j in range(i, n):
                curr_arr.append(nums[j])
                comb_sum = sum(curr_arr)
                if comb_sum > target:
                    return
                elif comb_sum == target:
                    result.append(curr_arr)
                    return
                dfs(curr_arr.copy(), j)
                curr_arr.pop()
            return

        dfs([], 0)
        return result