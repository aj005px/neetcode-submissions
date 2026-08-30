class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            target = l+(r-l)//2
            if nums[target]<nums[r]:
                r=target
            else:
                l = target+1
        return nums[l]