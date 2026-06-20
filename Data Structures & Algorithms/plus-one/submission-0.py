class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1

        for i in range(len(digits) - 1, -1, -1):
            add = digits[i] + remainder
            digits[i] = add % 10
            remainder = add // 10

        if remainder:
            digits.insert(0, 1)

        return digits