class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = list(Counter(arr).values())
        heapq.heapify(heap)
        while k:
            if not heap:
                break
            c = heapq.heappop(heap)
            k -= c
            if k < 0:
                return len(heap) + 1
        return len(heap)
