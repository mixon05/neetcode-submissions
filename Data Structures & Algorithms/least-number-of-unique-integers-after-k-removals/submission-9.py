class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = [(count, num) for num, count in Counter(arr).items()]
        heapq.heapify(heap)
        while k:
            if not heap:
                break
            c, v = heapq.heappop(heap)
            if k - c >= 0:
                k -= c
            else:
                return len(heap) + 1
        return len(heap)
