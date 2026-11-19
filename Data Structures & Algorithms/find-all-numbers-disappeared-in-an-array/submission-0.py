class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans =[]
        for i in range(0,len(nums)):
            if i+1 not in nums:
                ans.append(i+1)
        return ans