class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        heap = []
        for i in range(len(workers)):
            worker_x, worker_y = workers[i]
            for j in range(len(bikes)):
                bike_x, bike_y = bikes[j]
                distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)
                heap.append((distance, i, j))
        heapq.heapify(heap)
        w_s = set()
        b_s = set() 
        res = [0] * len(workers)
        while len(w_s) != len(workers):
            d, worker, bike = heapq.heappop(heap)
            if worker not in w_s and bike not in b_s:
                res[worker] = bike
                w_s.add(worker)
                b_s.add(bike)
        return res