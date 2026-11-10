class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            diff = abs(x - y)
            if diff:
                heapq.heappush_max(stones, diff)
        return stones[0] if len(stones) == 1 else 0