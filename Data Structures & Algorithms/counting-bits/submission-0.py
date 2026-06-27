class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(0, n+1):
            ans.append(str(bin(num)[2:]).count("1"))
        return ans
        