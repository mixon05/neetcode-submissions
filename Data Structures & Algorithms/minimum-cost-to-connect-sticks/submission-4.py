class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) != 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            curr_cost = x + y
            cost += curr_cost
            heapq.heappush(sticks, curr_cost)
        return cost
