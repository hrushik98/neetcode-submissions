class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ans1 = 0
        for i in nums:
            ans1 = ans1 ^ i
        
        ans2 = 0
        for i in range(0,len(nums)+1):
            ans2 = ans2 ^ i
        
        final = ans1 ^ ans2
        return final