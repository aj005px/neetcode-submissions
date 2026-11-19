class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        pos = {}

        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    pos[i] = j

        for i, j in pos.items():
            for k in range(j+1, len(nums2)):
                if nums2[k] > i:
                    ans.append(nums2[k])
                    break
            else:
                ans.append(-1)

        return ans