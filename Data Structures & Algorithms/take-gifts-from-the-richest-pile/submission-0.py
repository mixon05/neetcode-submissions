class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            val = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, floor(sqrt(val)))
        return sum(gifts)