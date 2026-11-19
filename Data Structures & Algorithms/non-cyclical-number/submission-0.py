class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            visited.add(n)
            n = sum(int(x)*int(x) for x in str(n))
            if n in visited:
                return False
        return True