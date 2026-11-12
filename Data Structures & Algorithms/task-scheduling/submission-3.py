class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = list(Counter(tasks).values())
        heapq.heapify_max(heap)
        cycles = 0
        queue = deque()
        while heap or queue:
            cycles += 1
            if queue and queue[0][1] == cycles:
                heapq.heappush_max(heap, queue.popleft()[0])
            if heap:
                task = heapq.heappop_max(heap)
                if task != 1:
                    queue.append((task - 1, cycles + n + 1))
        return cycles
        