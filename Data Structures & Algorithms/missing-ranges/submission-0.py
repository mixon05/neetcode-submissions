class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        res = []
        left_bound = lower
        for n in nums:
            if n != left_bound:
                res.append([left_bound, n - 1])
            left_bound = n + 1
        if nums[-1] != upper:
            res.append([nums[-1] + 1, upper])
        return res