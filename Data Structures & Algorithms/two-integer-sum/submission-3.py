class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index, n in enumerate(nums):
            to_find = target - n
            if to_find in hmap:
                return sorted([index, hmap[to_find]])
            else:
                hmap[n] = index
            
