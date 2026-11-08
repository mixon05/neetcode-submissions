class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        def dfs(curr_str, left):
            if left == 0:
                result.add(curr_str)
                return
            for i in range(len(curr_str)):
                dfs(curr_str[:i] + "()" + curr_str[i:], left - 1)
        dfs("()", n - 1)
        return list(result)