class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        return str(b).count("1")
        