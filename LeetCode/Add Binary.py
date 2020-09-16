class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aint, bint = int(a, 2), int(b,2)
        return bin(aint + bint)[2:]