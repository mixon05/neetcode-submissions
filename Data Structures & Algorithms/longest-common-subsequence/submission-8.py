class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        curr_row = [0] * (len(text2) + 1)
        prev_row = [0] * (len(text2) + 1)
        for r in range(len(text1) - 1, -1, -1):
            for c in range(len(text2) - 1, -1, -1):
                if text1[r] == text2[c]:
                    curr_row[c] = 1 + prev_row[c + 1]
                else:
                    curr_row[c] = max(prev_row[c], curr_row[c + 1])
            prev_row = curr_row.copy()
        return prev_row[0]