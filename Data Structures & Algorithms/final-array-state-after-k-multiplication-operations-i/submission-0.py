class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(v, i) for (i, v) in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            heapq.heappush(heap, (val * multiplier, idx))
        return list(map(lambda tup: tup[0], sorted(heap, key=lambda tup: tup[1])))