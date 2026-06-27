class Solution:
    def mySqrt(self, x: int) -> int:
        ans = x
        while ans*ans > x:
            ans = (ans + x//ans) >> 1
        return ans

        