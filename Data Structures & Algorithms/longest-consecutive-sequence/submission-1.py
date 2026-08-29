class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = 1
        max_res = 1
        nums = sorted(nums)

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                res += 1
            elif nums[i + 1] - nums[i] == 0:
                continue
            else:
                max_res = max(max_res, res)
                res = 1

        return max(max_res, res)
