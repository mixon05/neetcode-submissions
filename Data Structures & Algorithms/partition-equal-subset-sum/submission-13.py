class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum = sum(nums)
        if list_sum % 2 != 0:
            return False
        half_sum = list_sum / 2
        sums = set()
        sums.add(0)
        for num in nums:
            curr_sums = set()
            for s in sums:
                new_sum = s + num
                if new_sum == half_sum:
                    return True
                curr_sums.add(new_sum)
            sums |= curr_sums
        return False