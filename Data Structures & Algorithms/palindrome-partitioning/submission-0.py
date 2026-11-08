class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr = []
        def dfs(start):
            if start == len(s):
                result.append(curr.copy())
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    curr.append(sub)
                    dfs(end)
                    curr.pop()
        dfs(0)
        return result