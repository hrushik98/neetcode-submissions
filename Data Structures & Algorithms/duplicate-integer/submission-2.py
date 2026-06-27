class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        window = set()
        for num in nums:
            if num not in window:
                window.add(num)
            else:
                return True
        return False