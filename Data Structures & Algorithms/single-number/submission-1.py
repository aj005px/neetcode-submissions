class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #bit manipulation

        ans = 0

        for i in nums:
            ans = i^ans
        return ans