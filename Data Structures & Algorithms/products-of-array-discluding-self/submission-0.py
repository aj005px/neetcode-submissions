class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = nums.count(0)

        for x in nums:
            if x != 0:
                prod *= x

        for j in range(len(nums)):
            if zero_count > 1:
                nums[j] = 0
            elif zero_count == 1:
                if nums[j] == 0:
                    nums[j] = prod
                else:
                    nums[j] = 0
            else:
                nums[j] = prod // nums[j]

        return nums
