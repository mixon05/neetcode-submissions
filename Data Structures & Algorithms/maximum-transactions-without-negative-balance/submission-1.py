class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        res = 0
        b = 0
        heap = []
        for t in transactions:
            b += t
            res += 1
            heapq.heappush(heap, t)
            if b < 0:
                worst = heapq.heappop(heap)
                b -= worst
                res -= 1
        return res
