class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sort = sorted(nums)
        if nums == sort or nums == sort[::-1]:
            return True
        return False
        