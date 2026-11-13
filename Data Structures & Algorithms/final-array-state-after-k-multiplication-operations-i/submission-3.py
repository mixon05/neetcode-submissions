class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums.copy()
        heap = [(v, i) for (i, v) in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            n, i = heapq.heappop(heap)
            res[i] *= multiplier
            heapq.heappush(heap, (res[i], i))
        return res
        