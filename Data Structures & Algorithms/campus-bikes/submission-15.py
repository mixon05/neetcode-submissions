class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        heap = []
        n = len(workers)
        for i in range(n):
            worker_x, worker_y = workers[i]
            for j in range(len(bikes)):
                bike_x, bike_y = bikes[j]
                distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)
                heap.append((distance, i, j))
        heap.sort()
        w_s = set()
        b_s = set() 
        res = [0] * n
        while len(w_s) != n:
            d, worker, bike = heapq.heappop(heap)
            if worker not in w_s and bike not in b_s:
                res[worker] = bike
                w_s.add(worker)
                b_s.add(bike)
        return res