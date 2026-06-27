class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxs = []
        cnt = 0
        for x in nums:
            if x == 1:
                cnt+=1
            elif x == 0:
                maxs.append(cnt)
                cnt = 0

        maxs.append(cnt) 

        return max(maxs)     


        