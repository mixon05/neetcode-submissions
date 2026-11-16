class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        dp = {}
        res = 0
        i = 0
        for r in range(rows):
            times = 0
            start_idx = i
            space_left = cols

            if start_idx in dp:
                times, next_idx = dp[start_idx]
                res += times
                i = next_idx
                continue

            while space_left > 0:
                if space_left >= len(sentence[i]):
                    space_left -= len(sentence[i]) + 1
                    i += 1
                    if i == len(sentence):
                        times += 1
                        i = 0
                else:
                    break
            res += times
            dp[start_idx] = (times, i)
        return res