class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastIndex = len(digits) - 1
        while digits[lastIndex] == 9:
            digits[lastIndex] = 0
            if lastIndex == 0:
                digits.insert(0, 1)
                return digits
            lastIndex -= 1
        digits[lastIndex] += 1
        return digits
