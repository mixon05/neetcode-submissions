class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        curr_arr = [None] * n
        visited = set()
        def dfs(idx):
            if idx == n:
                result.append(curr_arr.copy())
                return
            for i in range(n):
                val = nums[i]
                if val in visited:
                    continue
                curr_arr[idx] = val
                visited.add(val)
                dfs(idx + 1)
                visited.remove(val)
                curr_arr[idx] = None
        dfs(0)
        return result