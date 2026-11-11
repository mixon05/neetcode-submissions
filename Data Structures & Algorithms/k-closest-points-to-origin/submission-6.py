class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = x**2 + y**2
            heap.append((dist, x, y))
        heapq.heapify(heap)
        while k > 0:
            res.append(heapq.heappop(heap)[1:])
            k -= 1
        return res