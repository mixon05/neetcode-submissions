class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr_arr = []
        visited = set()
        def dfs():
            if len(curr_arr) == len(nums):
                result.append(curr_arr.copy())
                return
            for i in range(len(nums)):
                val = nums[i]
                if val in visited:
                    continue
                curr_arr.append(val)
                visited.add(val)
                dfs()
                visited.remove(val)
                curr_arr.pop()
        dfs()
        return result