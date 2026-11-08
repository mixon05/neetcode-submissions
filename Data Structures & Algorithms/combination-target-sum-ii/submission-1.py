class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        curr_arr = []
        def dfs(i, left):
            if left == 0:
                result.append(curr_arr.copy())
            for j in range(i, len(candidates)):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                if left < candidates[j]:
                    return
                curr_arr.append(candidates[j])
                dfs(j + 1, left - candidates[j])
                curr_arr.pop()
        dfs(0, target)
        return result
