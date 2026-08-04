class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        one, two = 2, 3  # ways to reach step 2 and 3

        for _ in range(4, n + 1):
            one, two = two, one + two

        return two