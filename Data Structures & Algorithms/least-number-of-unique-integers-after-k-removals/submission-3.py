class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = [(count, num) for num, count in Counter(arr).items()]
        heapq.heapify(heap)
        for _ in range(k):
            if not heap:
                break
            c, v = heapq.heappop(heap)
            c -= 1
            if c:
                heapq.heappush(heap, (c, v))

        return len(heap)
