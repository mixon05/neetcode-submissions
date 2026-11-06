class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right - 1)
        
        def pal_len(x):
            return x[1] - x[0] + 1

        longest = (0, 0)
        for i in range(len(s)):
            idx = expand(i, i)
            longest = idx if pal_len(idx) > pal_len(longest) else longest
            if i < len(s) - 1 and s[i] == s[i + 1]:
                idx = expand(i, i + 1)
                longest = idx if pal_len(idx) > pal_len(longest) else longest
        return s[longest[0]:longest[1] + 1]