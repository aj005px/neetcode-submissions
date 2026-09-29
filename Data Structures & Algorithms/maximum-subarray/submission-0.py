class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curentsum = 0
        maxsub = nums[0]

        for i in range(len(nums)):
            if curentsum < 0:
                curentsum = 0
            
            curentsum += nums[i]
            maxsub = max(maxsub,curentsum)

        return maxsub