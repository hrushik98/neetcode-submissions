class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        if not nums:
            return 
        for index, number in enumerate(nums):
            toFind = target - number
            if toFind in hmap.keys():
                return sorted([hmap[toFind], index])
            else:
                hmap[number] = index
        