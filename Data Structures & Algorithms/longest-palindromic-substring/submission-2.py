class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def longest_pal_1(i):
            dist = 1
            while i - dist >= 0 and i + dist < len(s):
                if s[i - dist] != s[i + dist]:
                    return s[i - dist + 1 : i + dist]
                dist += 1
            return s[i - dist + 1 : i + dist]

        def longest_pal_2(i, j):
            dist = 1
            while i - dist >= 0 and j + dist < len(s):
                if s[i - dist] != s[j + dist]:
                    return s[i - dist + 1 : j + dist]
                dist += 1
            return s[i - dist + 1 : j + dist]

        longest = ""
        for i in range(len(s)):
            new_str = longest_pal_1(i)
            longest = new_str if len(new_str) > len(longest) else longest
            if i + 1 < len(s) and s[i] == s[i + 1]:
                new_str = longest_pal_2(i, i + 1)
                longest = new_str if len(new_str) > len(longest) else longest 
        return longest