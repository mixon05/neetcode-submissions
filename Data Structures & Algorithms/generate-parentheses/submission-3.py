class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr_arr = []
        def dfs(left, right):
            if left == 0 and right == 0:
                result.append("".join(curr_arr))
                return
            if left > 0:
                curr_arr.append("(")
                dfs(left - 1, right)
                curr_arr.pop()
            if right > left:
                curr_arr.append(")")
                dfs(left, right - 1)
                curr_arr.pop()
        dfs(n, n)
        return result