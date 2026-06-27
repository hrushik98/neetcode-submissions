class Solution:
    def countBits(self, n: int) -> List[int]:
        return [ str(bin(num)[2:]).count("1") for num in range(n+1)]