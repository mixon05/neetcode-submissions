from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map = defaultdict(list)
        heap = []
        res = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            map[dist].append([x, y])
            heap.append(dist)
        heapq.heapify(heap)
        while k > 0:
            res.append(map[heapq.heappop(heap)].pop())
            k -= 1
        return res

        