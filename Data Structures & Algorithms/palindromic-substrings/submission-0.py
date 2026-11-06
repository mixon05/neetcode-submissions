class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        subs_count = 0

        def expand(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            subs_count += expand(i, i)
            if i < n - 1 and s[i] == s[i + 1]:
                subs_count += expand(i, i + 1)
        return subs_count