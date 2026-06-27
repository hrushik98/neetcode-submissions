class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index, num in enumerate(nums):
            tofind = target - num
            if tofind in hmap:
                return [hmap[tofind] , index]
            else:
                hmap[num] = index

