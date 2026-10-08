class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = 0

        for i in nums[:]:
            if i == 0:
                zero_count += 1
                nums.remove(i)
        
        for i in range(zero_count):
            nums.append(0)
        
        return nums
        