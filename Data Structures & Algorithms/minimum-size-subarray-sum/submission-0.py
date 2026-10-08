class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        res = float('inf')

        for r in range(len(nums)):
            s += nums[r]
            while s>=target:
                res = min(r-l+1,res)
                s -= nums[l]
                l+=1
        return 0 if res == float('inf') else res