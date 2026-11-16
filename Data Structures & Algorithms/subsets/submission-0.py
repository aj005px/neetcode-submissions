class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def back(i,p):
            if i == len(nums):
                result.append(p[:])
                return

            p.append(nums[i])
            back(i+1,p)
            p.pop()

            back(i+1,p)
        back(0,[])
        return result