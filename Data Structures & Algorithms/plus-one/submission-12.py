from itertools import chain

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += carry
                return digits
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
        return list(chain([carry], digits))
