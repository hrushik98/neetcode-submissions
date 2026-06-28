class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(x.lower() for x in s if x.isalnum() )
        l = 0
        r = len(s)-1
        while l<r and l>=0 and r>0:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True 