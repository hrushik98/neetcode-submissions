class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index, n in enumerate(nums):
            toFind = target - n
            if toFind in hmap:
                return [hmap[toFind], index]
            else:
                hmap[n] = index
