class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        occ = defaultdict(int)
        for c in s:
            occ[c] += 1
        for c in t:
            if occ[c] == 0:
                return False
            occ[c] -= 1
        return True
