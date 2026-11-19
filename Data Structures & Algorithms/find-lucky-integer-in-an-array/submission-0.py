class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max_ans = -1
        for i in arr:
            if arr.count(i) == i:
                max_ans = max(max_ans,i)
        return max_ans