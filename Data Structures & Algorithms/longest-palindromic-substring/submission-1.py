class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def longest_pal_1(i):
            dist = 1
            output = s[i]
            while i - dist >= 0 and i + dist < len(s):
                if s[i - dist] != s[i + dist]:
                    return output
                output = s[i - dist] + output + s[i + dist]
                dist += 1
            return output

        def longest_pal_2(i, j):
            dist = 1
            output = s[i] + s[j]
            while i - dist >= 0 and j + dist < len(s):
                if s[i - dist] != s[j + dist]:
                    return output
                output = s[i - dist] + output + s[j + dist]
                dist += 1
            return output

        longest = ""
        for i in range(len(s)):
            new_str = longest_pal_1(i)
            longest = new_str if len(new_str) > len(longest) else longest
            if i + 1 < len(s) and s[i] == s[i + 1]:
                new_str = longest_pal_2(i, i + 1)
                longest = new_str if len(new_str) > len(longest) else longest 
        return longest