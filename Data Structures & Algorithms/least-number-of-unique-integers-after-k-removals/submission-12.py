class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted(Counter(arr).values())
        for i, c in enumerate(counts):
            k -= c
            if k < 0:
                return len(counts) - i
        return 0
