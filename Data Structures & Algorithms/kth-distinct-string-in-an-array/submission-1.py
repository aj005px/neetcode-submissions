class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = []
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                distinct.append(arr[i])
        

        if len(distinct) >= k:
            return distinct[k-1]

        return ""
                