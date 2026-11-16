class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        buckets = [[] for _ in range(2000)]
        n = len(workers)
        for i in range(n):
            worker_x, worker_y = workers[i]
            for j in range(len(bikes)):
                bike_x, bike_y = bikes[j]
                distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)
                buckets[distance].append((i, j))
        w_s = set()
        b_s = set() 
        res = [0] * n
        for bucket in buckets:
            for worker, bike in bucket:
                if worker not in w_s and bike not in b_s:
                    res[worker] = bike
                    w_s.add(worker)
                    b_s.add(bike)
            if len(w_s) == n:
                break
        return res