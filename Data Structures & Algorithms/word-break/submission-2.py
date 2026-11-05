class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = set()
        def dfs(rest):
            if not rest:
                return True
            if rest in dp:
                return False
            for word in wordDict:
                if rest.startswith(word):
                    stripped_prefix = rest.removeprefix(word)
                    if dfs(stripped_prefix):
                        return True
                    dp.add(stripped_prefix)
            return False
        return dfs(s)