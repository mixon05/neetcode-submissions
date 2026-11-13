class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            res.append(s % 10)
            carry = s // 10
        if carry:
            res.append(carry)
        res.reverse()
        return res