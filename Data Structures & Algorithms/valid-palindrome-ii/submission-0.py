class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(s, left, right):
            l = left
            r = right
            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1 
                r -=1 
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPal(s, left+1, right) or isPal(s,left, right-1)
            left +=1
            right -=1
        return True

        