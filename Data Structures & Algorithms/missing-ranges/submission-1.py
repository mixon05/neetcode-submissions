from itertools import chain

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        stream = chain([lower - 1], nums, [upper + 1])
        prev = next(stream)
        for curr in stream:
            if curr - prev > 1:
                res.append([prev + 1, curr - 1])
            prev = curr
        return res
            