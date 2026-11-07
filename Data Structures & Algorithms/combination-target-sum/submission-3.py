class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def dfs(curr_arr, i, left):
            for j in range(i, n):
                if left < nums[j]:
                    return
                elif left == nums[j]:
                    curr_arr.append(nums[j])
                    result.append(curr_arr.copy())
                    curr_arr.pop()
                    return
                curr_arr.append(nums[j])
                dfs(curr_arr, j, left - nums[j])
                curr_arr.pop()
            return

        dfs([], 0, target)
        return result