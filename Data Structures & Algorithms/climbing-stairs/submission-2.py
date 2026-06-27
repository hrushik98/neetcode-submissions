class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def fib(n):
            if n in mem:
                return mem[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            mem[n] =  fib(n-1)+fib(n-2)
            return mem[n]
        
        return fib(n+1)
        