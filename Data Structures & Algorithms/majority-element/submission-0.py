class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        answer = 0

        for i in range(len(nums)):
            count = nums.count(nums[i])

            if count > max_count:
                max_count = count
                answer = nums[i]

        return answer
