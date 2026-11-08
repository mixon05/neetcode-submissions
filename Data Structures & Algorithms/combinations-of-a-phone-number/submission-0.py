class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []
        curr = []
        def dfs(i):
            if i == len(digits):
                result.append("".join(curr))
                return
            for l in digits_map[digits[i]]:
                curr.append(l)
                dfs(i + 1)
                curr.pop()
        dfs(0)
        return result