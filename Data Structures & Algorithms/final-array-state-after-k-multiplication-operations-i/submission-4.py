class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(v, i) for (i, v) in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            n, i = heapq.heappop(heap)
            nums[i] *= multiplier
            heapq.heappush(heap, (nums[i], i))
        return nums
        