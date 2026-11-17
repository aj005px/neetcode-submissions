class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def back(i,path,total):
            if target == total:
                ans.append(path[:])
                return

            if i>=len(nums) or total >target:
                return

            
            path.append(nums[i])
            back(i,path,total+nums[i])
            path.pop()
            back(i+1,path,total)

        
        back(0,[],0)

        return ans
            
                    
                
        